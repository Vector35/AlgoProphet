from binaryninja import *
from binaryninja.binaryview import BinaryView
from . import dfg, graph_match
import os, sys

from binaryninja.interaction import MultilineTextField, TextLineField
from binaryninjaui import UIActionHandler, UIAction, UIActionContext

ignore_list = list()
inst_tag_list = dict()

PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))

'''
ignore function included in the list
'''
def get_ignore_list():
    global ignore_list
    with open(os.path.join(PLUGINDIR_PATH, "ignore.txt")) as f:
        lines = f.readlines()
        for l in lines:
            ignore_list.append(l.strip())
    f.close()

'''
load previous tag list from bndb
'''
def load_inst_tag_list(bv: BinaryView, addr):
    global inst_tag_list
    l = bv.get_user_data_tags_at(addr)
    if len(l) != 0:
        if addr not in inst_tag_list:
            inst_tag_list[addr] = list()
        for i in range(len(l)):
            inst_tag_list[addr].append(l[i].data)

'''
add tag to instruction if model still not identified
'''
def add_model_tag_to_inst(bv: BinaryView, addr, model, user_tag):
    global inst_tag_list
    load_inst_tag_list(bv, addr)
    if addr not in inst_tag_list:
        inst_tag_list[addr] = list()
    if model in inst_tag_list[addr]:
        return
    inst_tag_list[addr].append(model)
    bv.create_user_data_tag(addr, user_tag, f'{model}')


def matcher(bv: BinaryView, f_dfg, f, user_tag):
    for matched_model, matched_inst in graph_match.match(f_dfg).items():
        if len(matched_inst) != 0:
            print("AlgoProphet: Find ", matched_model, " in ", f.name)
            for idx in matched_inst:
                print("Exception: ", idx)
                address = f.mlil.ssa_form[idx].address
                print("address: ", hex(address))
                add_model_tag_to_inst(bv, address, matched_model, user_tag)

'''
iterate all functions from binary and match models
'''
def function_iterator(bv: BinaryView):
    # dfg for all functions in current binary
    print(bv)
    # create user tag if not exist
    if bv.get_tag_type("AlgoProphet") == None:
        bv.create_tag_type("AlgoProphet", "🥧")
    tag = bv.get_tag_type("AlgoProphet")
    get_ignore_list()
    for f in bv.functions:
        if f.name in ignore_list:
            continue
        matcher(bv, dfg.read_binaryview(bv, f), f, tag)
        dfg.clean_data()
                
def match_helper(ctx: UIActionContext):
    if ctx is None or ctx.context is None or ctx.binaryView is None or ctx.function is None or ctx.address is None:
        print("click the binary view!!")
        return
    function_iterator(ctx.binaryView)
    
def model_generator(bv, f, instr_list):
    f_dfg = dfg.read_binaryview(bv, f)
    print(f_dfg)
    # start filter dfg with instr_list
    # cancel would close binary ninja window?
    
def build_helper(ctx: UIActionContext):
    if ctx is None or ctx.context is None or ctx.binaryView is None or ctx.function is None or ctx.address is None:
        print("click the binary view!!")
        return
    bv = ctx.binaryView
    func_name = TextLineField("Specify function name")
    input_list = MultilineTextField("Specify instruction indexes")
    get_form_input([func_name, input_list], "AlgoProphet")
    f = bv.get_functions_by_name(func_name.result)[0]
    print("Build current model on function: ", f.name)
    print("model instructions: ", input_list.result.split("\n"))
    md_instr_list = list()
    for i in input_list.result.split("\n"):
        if not (i.isdigit()):
            print(i, " is not a number")
        else:
            if (int(i) < 0) or (int(i) >= len(list(f.mlil.ssa_form.instructions))):
                print(i, " is out of the range of function")
            else:
                md_instr_list.append(int(i))
    model_generator(bv, f, md_instr_list)
                
UIAction.registerAction("AlgoProphet: Match Algos")
UIAction.registerAction("AlgoProphet: Build models")
UIActionHandler.globalActions().bindAction("AlgoProphet: Match Algos", UIAction(match_helper))
UIActionHandler.globalActions().bindAction("AlgoProphet: Build a model", UIAction(build_helper))