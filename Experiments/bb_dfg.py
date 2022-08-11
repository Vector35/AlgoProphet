from cmath import e
import os, sys
import logging
import networkx as nx
import matplotlib.pyplot as plt
from numpy import power, true_divide

os.environ['BN_DISABLE_USER_PLUGINS'] = '1'

import binaryninja as bn
from binaryninja import *

debug = True
arnode = {}
nodes = []
exit_nodes = []
input_vars = []
load_mode = False
current_data_width = 0
parent_dict = {}

opmap = {
    "SUB": "ADD",
    "FSUB": "FADD",
    "DIV": "MUL",
    "FDIV": "FMUL",
}

graph = nx.DiGraph()

# each operation should have unique name
def get_next_opname(operation):
    global arnode
    if operation in arnode:
        arnode[operation] += 1
    else:
        arnode[operation] = 0
    return operation + "#" + str(arnode[operation])

def get_next_func(fun):
    global funnode
    if fun in funnode:
        funnode[fun] += 1
    else:
        funnode[fun] = 0
    return fun + "#" + str(funnode[fun])

def get_arithmetic(operation):
    global graph
    op = str(operation).split(".")[1][5:]
    if op in opmap.keys():
        if str(-1) not in nodes:
            nodes.append(str(-1))
        if op in ["SUB", "FSUB"]:
            opnode1 = get_next_opname("MUL")
        elif op in ["DIV", "FDIV"]:
            opnode1 = get_next_opname("pow")
        opnode2 = get_next_opname(opmap[op])
        # add nodes and edges
        add_node_with_attr(opnode1, opnode2)
        add_edge_node(opnode1, opnode2)
        add_node_with_attr(str(-1), opnode1)
        add_edge_node(str(-1), opnode1)
        return opnode1 + "/" + opnode2
    else:
        return get_next_opname(op)

def update_dict(node, parent):
    global parent_dict
    if node not in parent_dict:
        parent_dict[node] = []
    if parent not in parent_dict[node]:
        parent_dict[node].append(parent)

def get_top_parents(node, parents):
    if str(node) in nodes:
        parents.append(node)
    else:
        if node in parent_dict:
            for p in parent_dict[node]:
                parents = get_top_parents(p, parents)
    return parents

def add_node_with_attr(node1, node2):
    global graph, input_vars
    # add two nodes to graph
    for node in [node1, node2]:
        if '#' not in node:
            graph.add_node(node, type="constant", value=node)
        elif node in input_vars:
            graph.add_node(node, type="ssavar", value=node)
        else:
            graph.add_node(node, type="operation", value=node.split('#')[0])

def add_edge_node(node1, node2):
    global graph
    if "#" in str(node1):
        hash_node1 = node1.split("#")[0]
    else:
        hash_node1 = node1
        
    if "#" in str(node2):
        hash_node2 = node2.split("#")[0]
    else:
        hash_node2 = node2

    if hash_node1 != hash_node2:
        # add nodes
        add_node_with_attr(node1, node2)
        # add edges
        graph.add_edge(node1, node2, weight=1)
    else:
        # if the two are same operation nodes
        # merge node and sum up the weights on two edges
        for in_edge in graph.in_edges(node1):
            if graph.has_edge(in_edge[0], node2):
                w = graph[in_edge[0]][node2]["weight"]
                graph[in_edge[0]][node2]["weight"] = w + 1
            else:
                # add nodes
                add_node_with_attr(in_edge[0], node2)
                # add edges
                graph.add_edge(in_edge[0], node2, weight=graph[in_edge[0]][node1]["weight"])
        graph.remove_node(node1)

def bridge_parent_to_arith(operand, arith):
    global graph
    for parent in get_top_parents(operand, list()):
        # add edges
        if graph.has_edge(parent, arith):
            w = graph[parent][arith]["weight"]
            graph[parent][arith]["weight"] = w + 1
        else:
            # add nodes
            add_node_with_attr(parent, arith)
            # add edges
            add_edge_node(parent, arith)

def rhs_visit(expr):
    global graph
    global nodes
    global parent_dict
    global load_mode
    if isinstance(expr, MediumLevelILVarSsa):
        return str(expr)
    elif isinstance(expr, MediumLevelILVarSsaField):
        return expr.src.name + "#" + str(expr.src.version)
    elif isinstance(expr, MediumLevelILLoadSsa):
        load_mode = True
        rhs_output_node = rhs_visit(expr.src)
        operation = get_arithmetic("x.xxxx_load")
        nodes.append(operation)
        # add nodes
        add_node_with_attr(rhs_output_node, operation)
        # add edges
        add_edge_node(rhs_output_node, operation)
        load_mode = False
        return operation
    elif isinstance(expr, Constant):
        # temporarily replace shift positions to 1
        # because not able to identify data type working with index
        # though we are able to identify the type of ssavar
        if load_mode == True:
            if "1" not in nodes:
                nodes.append("1")
            return "1"
        if str(expr) not in nodes:
            nodes.append(str(expr.constant))
        return str(expr.constant)
    elif isinstance(expr, MediumLevelILIntToFloat) or isinstance(expr, MediumLevelILFloatToInt) or isinstance(expr, MediumLevelILBoolToInt) or isinstance(expr, MediumLevelILFloatConv):
        return rhs_visit(expr.src)
    elif isinstance(expr, MediumLevelILLowPart):
        return rhs_visit(expr.src)
    elif isinstance(expr, Arithmetic):
        arithmetic = get_arithmetic(expr.operation)
        if "/" in arithmetic:
            arith1 = arithmetic.split("/")[0]
            nodes.append(arith1)
            arith2 = arithmetic.split("/")[1]
            nodes.append(arith2)
            # second operand > sub
            rhs_operand_2 = rhs_visit(expr.operands[1])
            bridge_parent_to_arith(rhs_operand_2, arith1)
            # first operand > add
            rhs_operand_1 = rhs_visit(expr.operands[0])
            bridge_parent_to_arith(rhs_operand_1, arith2)
            arithmetic = arith2
        elif isinstance(expr, MediumLevelILNeg):
            # this is the case of SUB
            # NEG should only have single operand
            rhs_operand1 = rhs_visit(expr.operands[0])
            arithmetic = get_arithmetic("x.xxxxxMUL")
            nodes.append(arithmetic)
            if str(-1) not in nodes:
                nodes.append(str(-1))
            bridge_parent_to_arith(str(-1), arithmetic)
            bridge_parent_to_arith(rhs_operand1, arithmetic)
        else:
            nodes.append(arithmetic)
            for op in expr.operands:
                rhs_operand = rhs_visit(op)
                print(rhs_operand)
                bridge_parent_to_arith(rhs_operand, arithmetic)
        return arithmetic

def inst_visit(ssa):
    global graph
    global nodes
    global parent_dict
    global exit_nodes
    global load_mode
    print("instruction: ", str(ssa))
    match type(ssa):
        case bn.mediumlevelil.MediumLevelILRet:
            exit_nodes.append(str(ssa.src[0]))
            return
        case bn.mediumlevelil.MediumLevelILCallSsa:
            func_addr = ssa.dest.constant
            func_name = bv.get_function_at(func_addr).name
            fname = get_next_func(func_name)
            for param in ssa.params:
                # add edges
                if graph.has_edge(str(param), fname):
                    w = graph[str(param)][fname]["weight"]
                    graph[str(param)][fname]["weight"] = w + 1
                else:
                    # add nodes
                    add_node_with_attr(str(param), fname)
                    # add edges
                    add_edge_node(str(param), fname)
            for dst_var in ssa.vars_written:
                dvar = dst_var.name + "#" + str(dst_var.version)
                update_dict[dvar] = fname
            return
        case bn.mediumlevelil.MediumLevelILVarPhi:
            for s in ssa.src:
                update_dict(ssa.dest.name + "#" + str(ssa.dest.version), s.name + "#" + str(s.version))
            return
        case bn.mediumlevelil.MediumLevelILIntrinsicSsa:
            # intrinsic
            for dest_var in ssa.vars_written:
                for src_var in ssa.vars_read:
                    update_dict(dest_var.name + "#" + str(dest_var.version), src_var.name + "#" + str(src_var.version))
            return
        case bn.mediumlevelil.MediumLevelILSetVarSsa:
            rhs = ssa.src
            lhs = ssa.dest
            lvar = lhs.name + "#" + str(lhs.version)
            # cases for rhs
            if isinstance(rhs, Constant):
                #bn.mediumlevelil.MediumLevelILConst
                if str(rhs) not in nodes:
                    nodes.append(str(rhs.constant))
                update_dict(lvar, str(rhs.constant))
                return
            elif isinstance(rhs, MediumLevelILLoadSsa):
                #bn.mediumlevelil.MediumLevelILLoadSsa
                # load from memory e.g., array
                load_mode = True
                operation = get_arithmetic("x.xxxx_load")
                nodes.append(operation)
                for node in get_top_parents(rhs_visit(rhs.src), list()):
                    # add nodes
                    add_node_with_attr(node, operation)
                    # add edges
                    add_edge_node(node, operation)
                update_dict(lvar, operation)
                load_mode = False
                return
            elif isinstance(rhs, MediumLevelILVarSsaField):
                #bn.mediumlevelil.MediumLevelILVarSsaField
                for var_read in ssa.vars_read:
                    update_dict(lvar, var_read.name + "#" + str(var_read.version))
                return
            elif isinstance(rhs, MediumLevelILSx):
                update_dict(lvar, str(rhs))
                return
            elif isinstance(rhs, MediumLevelILVarSsa):
                #bn.mediumlevelil.MediumLevelILVarSsa
                update_dict(lvar, str(rhs))
                return
            elif isinstance(rhs, Arithmetic):
                rhs_output_node = rhs_visit(rhs)
                update_dict(lvar, rhs_output_node)
            else:
                return
        case _:
            return

# this works for single basic block
def get_function(insts, start, end, r_vars, w_vars, loop_vars):
    global nodes, graph
    # first, find out the input vars for the basic block
    idx = start
    while idx < end:
        for i in insts[idx].vars_read:
            if i not in r_vars:
                r_vars.append(i)
        for i in insts[idx].vars_written:
            if i not in w_vars:
                w_vars.append(i)
                # if def after use, there should be a loop
                if i in r_vars and i not in loop_vars:
                    loop_vars.append(i)
        idx += 1 
    return r_vars, w_vars, loop_vars
    

# return list for each loops
# each loop is a list of basic blocks
# eg:
# [[b0,b1,b2], [b7,b8,b9]] means two loops, the first with {b0,b1,b2}, the second with {b7,b8,b9}
def calculate_natural_loops(func):
    loops = []

    # find back edges (B -> A when A dominates B)
    # A is called "header", B is called "footer"
    #
    # WARNING:
    #   Basic_block.back_edge is a less strict "edge to ancestor" definition of back edge.
    #   We need the stricter "edge to dominator" definition for loop detection.
    back_edges = []
    for bb in func.basic_blocks:
        for edge in bb.outgoing_edges:
            if edge.target in edge.source.dominators:
                back_edges.append(edge)
                #print('back edge %s -> %s' % (bbstr(edge.source), bbstr(edge.target)))

    # reverse breadth-first search from footer to header, collecting all nodes
    for edge in back_edges:
        (header, footer) = (edge.target, edge.source)
        #print('collecting blocks for loop fenced between %s and %s:' % (bbstr(header), bbstr(footer)))
        loop_blocks = set([header, footer])
        if header != footer:
            queue = [edge.source]
            while queue:
                cur = queue.pop(0)
                loop_blocks.add(cur)
                new_batch = [e.source for e in cur.incoming_edges if (not e.source in loop_blocks)]
                #print('incoming blocks to %s: %s' % (bbstr(cur), [bbstr(x) for x in new_batch]))
                queue.extend(new_batch)
        #print(','.join([bbstr(n) for n in loop_blocks]))

        # store this loop
        loops.append(list(loop_blocks))

    return loops
    
def main():
    global graph, bv, bb_dict, debug, nodes, input_vars
    path = sys.argv[1]
    bv = BinaryViewType.get_view_of_file(path)
    func = sys.argv[2]
    exit_idx = sys.argv[3]
    arch = sys.argv[4]
    
    f = bv.get_functions_by_name(func)[0]
    insts = f.mlil.ssa_form
    
    if exit_idx == "-1":
        for loop in calculate_natural_loops(insts):
            start_list = {}
            for loop_block in loop:
                start_list[loop_block.start] = loop_block
            r_vars = list()
            w_vars = list()
            loop_vars = list()
            for start, block in sorted(start_list.items()):
                r_vars, w_vars, loop_vars = get_function(insts, start, block.end, r_vars, w_vars, loop_vars)
            # the variables which are read but not defined in BB are input variables
            for var in r_vars:
                if var not in w_vars:
                    nodes.append(var.name + "#" + str(var.version))
            print("Input vars: ", nodes)
            input_vars = nodes.copy()
            # visit all instructions in BB
            for start, block in sorted(start_list.items()):
                while start < block.end:
                    inst_visit(insts[start])
                    start += 1
            print("Loop vars: ", loop_vars)
            for loop_var in loop_vars:
                loop_var_name = loop_var.name + "#" + str(loop_var.version)
                if loop_var_name in parent_dict:
                    for parent in parent_dict[loop_var_name]:
                        if parent in nodes:
                            graph.add_edge(parent, parent, weight=1)
    else:
        ssa_blocks = insts.basic_blocks
        start = ssa_blocks[int(exit_idx)].start
        end = ssa_blocks[int(exit_idx)].end
        r_vars = list()
        w_vars = list()
        loop_vars = list()
        r_vars, w_vars, loop_vars = get_function(insts, start, end, r_vars, w_vars, loop_vars)
        # the variables which are read but not defined in BB are input variables
        for var in r_vars:
            if var not in w_vars:
                nodes.append(var.name + "#" + str(var.version))
        print("Input vars: ", nodes)
        input_vars = nodes.copy()
        # visit all instructions in BB
        while start < end:
            inst_visit(insts[start])
            start += 1

    print(list(nx.selfloop_edges(graph)))
    
    if debug == True:
        nx.write_gml(graph, "./samples/" + arch + "_" + func + exit_idx + ".gml")
        nx.draw(graph, with_labels = True)
        plt.savefig("./samples/" + arch + "_" + func + exit_idx + ".png")
        return
    
    nx.write_gml(graph, "./model/" + arch + "_" + func + exit_idx + ".gml")
    nx.draw(graph, with_labels = True)
    plt.savefig("./model/" + arch + "_" + func + exit_idx + ".png")
    
main()