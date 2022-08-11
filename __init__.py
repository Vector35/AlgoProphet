from binaryninja import *
from binaryninja.binaryview import BinaryView
from . import dfg, graph_match

from binaryninjaui import UIActionHandler, UIAction, UIActionContext

inst_tag_list = dict()

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
    for f in bv.functions:
        matcher(bv, dfg.read_binaryview(bv, f), f, tag)
        dfg.clean_data()
                
def match_helper(ctx: UIActionContext):
    function_iterator(ctx.binaryView)
                
UIAction.registerAction("Match Algos")
UIActionHandler.globalActions().bindAction("Match Algos", UIAction(match_helper))