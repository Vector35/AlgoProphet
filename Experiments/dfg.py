from cmath import e
from ctypes import pointer
import os, sys
import logging
import networkx as nx
import matplotlib.pyplot as plt
from numpy import power, true_divide

os.environ['BN_DISABLE_USER_PLUGINS'] = '1'

import binaryninja as bn
from binaryninja import *

debug = True
# current instruction index in function
inst_idx = -1
arnode = {}
funnode = {}
nodes = []
exit_nodes = []
# input_vars are used to save ssavar we want to show in graph
input_vars = []
# If load mode == True, then pointer shows base of load operation
load_mode = False
current_data_width = 0
pointer_base = ""
current_load = ""
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
    global graph, input_vars, pointer_base, current_data_width
    # add two nodes to graph
    for node in [node1, node2]:
        if '#' not in node:
            graph.add_node(node, type="constant", value=node, idx=inst_idx)
        elif node in input_vars:
            graph.add_node(node, type="ssavar", value=node, idx=inst_idx)
        else:
            if "load" in node and node not in graph.nodes():
                print("current data width:           ", current_data_width)
                graph.add_node(node, type="operation", value=node.split('#')[0], idx=inst_idx, base=pointer_base, base_width=current_data_width)
            else:
                graph.add_node(node, type="operation", value=node.split('#')[0], idx=inst_idx)

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
        graph.add_edge(node1, node2, weight=1, idx=inst_idx, src_name=node1, dst_name=node2)
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
                graph.add_edge(in_edge[0], node2, weight=graph[in_edge[0]][node1]["weight"], idx=inst_idx, src_name=in_edge[0], dst_name=node2)
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
    global pointer_base
    global current_load
    global current_data_width
    if isinstance(expr, MediumLevelILVarSsa):
        if load_mode == True:
            if isinstance(expr.expr_type, PointerType):
                # this is the pointer
                pointer_base = str(expr)
                pointer_type = str(expr.expr_type)
                # might depend on architecture?
                if "int" in pointer_type:
                    current_data_width = 4
                elif "float" in pointer_type:
                    current_data_width = 4
                elif "double" in pointer_type:
                    current_data_width = 8
        return str(expr)
    elif isinstance(expr, MediumLevelILVarSsaField):
        return expr.src.name + "#" + str(expr.src.version)
    elif isinstance(expr, MediumLevelILLoadSsa):
        load_mode = True
        rhs_output_node = rhs_visit(expr.src)
        operation = get_arithmetic("x.xxxx_load")
        current_load = operation
        nodes.append(operation)
        # add nodes
        add_node_with_attr(rhs_output_node, operation)
        # add edges
        add_edge_node(rhs_output_node, operation)
        load_mode = False
        return operation
    elif isinstance(expr, Constant):
        if str(expr) not in nodes:
            nodes.append(str(expr.constant))
        return str(expr.constant)
    elif isinstance(expr, MediumLevelILIntToFloat) or isinstance(expr, MediumLevelILFloatToInt) or isinstance(expr, MediumLevelILBoolToInt) or isinstance(expr, MediumLevelILFloatConv):
        return rhs_visit(expr.src)
    elif isinstance(expr, MediumLevelILLowPart):
        return rhs_visit(expr.src)
    elif isinstance(expr, Arithmetic):
        arithmetic = get_arithmetic(expr.operation)
        print(arithmetic)
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
    global current_data_width
    global current_load
    match type(ssa):
        case bn.mediumlevelil.MediumLevelILRet:
            exit_nodes.append(str(ssa.src[0]))
            return
        case bn.mediumlevelil.MediumLevelILCallSsa:
            func_addr = ssa.dest.constant
            func_name = bv.get_function_at(func_addr).name
            f_name = get_next_func(func_name)
            for param in ssa.params:
                # add edges
                if graph.has_edge(str(param), f_name):
                    w = graph[str(param)][f_name]["weight"]
                    graph[str(param)][f_name]["weight"] = w + 1
                else:
                    # add nodes
                    add_node_with_attr(str(param), f_name)
                    # add edges
                    add_edge_node(str(param), f_name)
            for dst_var in ssa.vars_written:
                dvar = dst_var.name + "#" + str(dst_var.version)
                update_dict(dvar, f_name)
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
                # load from memory e.g., array
                load_mode = True
                # the bytes each element takes for
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
                for var_read in ssa.vars_read:
                    update_dict(lvar, var_read.name + "#" + str(var_read.version))
                return
            elif isinstance(rhs, MediumLevelILSx) or isinstance(rhs, MediumLevelILZx):
                rhs_output_node = rhs_visit(rhs.src)
                update_dict(lvar, rhs_output_node)
                return
            elif isinstance(rhs, MediumLevelILVarSsa):
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

# use topo sorting to get the order of nodes in the CFG
def topo_order(func):
    result = []
    result_dict = {}
    iedges = [0]*len(func.basic_blocks)
    for b in func.basic_blocks:
        iedges[b.index] = len([e for e in b.incoming_edges if not e.back_edge])
    stack = [func.basic_blocks[0]]
    while stack:
        block = stack.pop()
        result.append(block.index)
        result_dict[block.index] = block
        for child in reversed([e.target for e in block.outgoing_edges]):
            iedges[child.index] -= 1
            if iedges[child.index] == 0:
                stack.append(child)
    return result, result_dict

def get_ancestors(n, visited):
    if n in visited:
        return visited
    anc = nx.ancestors(graph, n)
    if len(anc) == 0:
        return visited
    for a in anc:
        if a not in visited:
            visited.append(a)
    for v in visited:
        visited = get_ancestors(v, visited)
    return visited

def main():
    global graph, bv, bb_dict, debug, nodes, input_vars, inst_idx
    path = sys.argv[1]
    bv = BinaryViewType.get_view_of_file(path)
    func = sys.argv[2]
    arch = sys.argv[3]
    op_level = sys.argv[4]
    
    f = bv.get_functions_by_name(func)[0]
    
    bb_order, bb_dict = topo_order(f.mlil.ssa_form)
    
    # add parameters into nodes
    for param in f.parameter_vars.vars:
        nodes.append(param.name + "#0")
    
    insts = f.mlil.ssa_form
    
    loop_vars = list()
    # get loop vars
    for loop in calculate_natural_loops(insts):
        start_list = {}
        for loop_block in loop:
            start_list[loop_block.start] = loop_block
        r_vars = list()
        w_vars = list()
        
        for start, block in sorted(start_list.items()):
            r_vars, w_vars, lv = get_function(insts, start, block.end, r_vars, w_vars, loop_vars)
            for i in lv:
                if i not in loop_vars:
                    loop_vars.append(i)
    
    print("Loop vars: ", loop_vars)
    for loop_var in loop_vars:
        nodes.append(loop_var)
    print("Input vars: ", nodes)
    input_vars = nodes.copy()
    
    for bb_idx in bb_order:
        bb = bb_dict[bb_idx]
        idx = bb.start
        while idx < bb.end:
            print("index: ", idx, ": ", str(insts[idx]))
            inst_idx = idx
            inst_visit(insts[idx])
            idx += 1
        
    # for loop_var in loop_vars:
    #     loop_var_name = loop_var.name + "#" + str(loop_var.version)
    #     if loop_var_name in parent_dict:
    #         for parent in parent_dict[loop_var_name]:
    #             if parent in nodes:
    #                 add_node_with_attr(parent, parent)
    #                 graph.add_edge(parent, parent, weight=1)
    
    # normalize the array index cases
    # heuristics:
    # sort the nodes which are used in load operation
    # consider the maximum number as the shift width on the memory
    load_edges = list()
    for n in graph.nodes():
        if "load" in n:
            # remove edges toward load
            for e in graph.in_edges(n):
                if e not in load_edges:
                    load_edges.append(e)
    
    # remove load_edges from graph
    core = {}
    for e in load_edges:
        if e[0] not in core and "load" not in e[0]:
            core[ e[0] ] = e[1]
        graph.remove_edge(e[0], e[1])
    print("core: ", core)
    # remove connected components of cores
    for c in core:
        load_name = core[c]
        shift_candidates = list()
        undirected_graph = graph.copy().to_undirected()
        for connected_node in nx.node_connected_component(undirected_graph, c):
            if "LSL" in connected_node:
                for e in graph.in_edges(connected_node):
                    if e[0].isnumeric():
                        shift_candidates.append(pow(2, int(e[0])))
            elif connected_node.isnumeric():
                shift_candidates.append(int(connected_node))
        print("shift_cands: ", shift_candidates)
        shift_ = max(shift_candidates)
        graph.nodes[load_name]["shift_width"] = shift_

    # we should trace parents of exit_node at this point (after iterating all instructions)
    # nodes_include_exit = list()
    # subcore = list()
    # for exit_node in exit_nodes: 
    #     for p in get_top_parents(exit_node, list()):
    #         if p not in subcore:
    #             subcore.append(p)
    # print("Should include: ", subcore)
    # graph_ = graph.copy().to_undirected()
    # for n in subcore:
    #     if n in graph.nodes():
    #         for sn in list(nx.shortest_path(graph_, n).keys()):
    #             if sn not in nodes_include_exit:
    #                 nodes_include_exit.append(sn)
    
    # graph = graph.subgraph(nodes_include_exit)

    print("self loop edges: ", list(nx.selfloop_edges(graph)))
    
    if debug == True:
        nx.write_gml(graph, "./samples/function_based/" + arch + "_" + func + "_" + op_level + ".gml")
        nx.draw(graph, with_labels = True)
        plt.savefig("./samples/function_based/" + arch + "_" + func + "_" + op_level + ".png")
        return
    
    nx.write_gml(graph, "./model/" + arch + "_" + func + ".gml")
    nx.draw(graph, with_labels = True)
    plt.savefig("./model/" + arch + "_" + func + ".png")
    
main()