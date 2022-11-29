import re
from traceback import format_exc

from typing import List, Union

import os
import sys
import traceback
from dataclasses import dataclass

import networkx as nx

from binaryninjaui import (
    UIAction,
    UIActionContext,
    UIActionHandler,
    UIContext,
)
# from PySide6.QtWidgets import QWidget

from binaryninja.enums import (
    FunctionGraphType,
)

from binaryninja import (
    BinaryView,
    MultilineTextField,
    TextLineField,
    Function,
    MediumLevelILFunction,
    MediumLevelILInstruction,
    MediumLevelILBasicBlock,
    MediumLevelILSetVarSsa,
    PluginCommand,
    Settings,
    TagType,
    get_form_input,
)

try:
    import binaryninja

    __module__ = sys.modules[__name__]

    __logger = binaryninja.Logger(0, __module__.__name__)

    log = __logger.log
    log_debug = __logger.log_debug
    log_info = __logger.log_info
    log_warn = __logger.log_warn
    log_error = __logger.log_error
    log_alert = __logger.log_alert

    log_debug(f'Loaded {__module__}')
except:
    log_warn(format_exc())
    from binaryninja import log_alert, log_debug, log_error, log_info, log_warn
    log = log_info


def print(*args, **kwargs):
    import io
    log_levels = {
        'alert': log_alert,
        'debug': log_debug,
        'error': log_error,
        'info': log_info,
        'warn': log_warn
    }
    if args and args[0] in log_levels:
        logger = log_levels[args[0]]
        args = args[1:]
    else:
        logger = log_debug
    with io.StringIO() as f:
        kwargs['file'] = f
        caller = ''
        if logger == log_debug:
            import inspect
            frame = inspect.stack()[1]
            if frame.function:
                if frame.lineno:
                    caller = f'[{frame.function}:{frame.lineno}]: '
                else:
                    caller = f'[{frame.function}]: '
            else:
                caller = ''
        import builtins
        builtins.print(*args, **kwargs)
        logger(caller + f.getvalue())


PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))

Settings().register_group("algoprophet", "AlgoProphet")

Settings().register_setting(
    "algoprophet.userFolderPath",
    """
    {
        "title" : "User Model Folder",
        "description" : "Path to folder for storing user model files.",
        "default" : "",
        "type" : "string"
    }
""",
)

Settings().register_setting(
    "algoprophet.ignoreFunctionNames",
    """
    {
        "title" : "Ignore Function Names",
        "description" : "List of function names to ignore during algorithm matching.",
        "type" : "array",
        "elementType" : "string",
        "default" : ["register_tm_clones", "deregister_tm_clones", "_init", "_start", "__libc_start_main", "__do_global_dtors_aux", "__cxa_finalize", "__gmon_start__", "__printf_chk", "__stack_chk_fail", "__stack_chk_guard", "_fini", "_ftext", "abort", "call_weak_fn", "frame_dummy", "time"]
    }
""",
)


def get_algoprophet_path(*components, allow_default: bool = True) -> str:
    path = Settings().get_string("algoprophet.userFolderPath")
    if not path and allow_default:
        path = PLUGINDIR_PATH
    if path:
        return os.path.join(path, *components)
    return None


from . import (
    dfg,
    dfg_processor,
    graph_match,
    # model_browser,
)


# inst_tag_list = dict()


@dataclass
class SelectionState:
    function: MediumLevelILFunction
    blocks: list
    instructions: list


Subject = Union[
    Function, MediumLevelILFunction, MediumLevelILInstruction, MediumLevelILBasicBlock
]


def get_ignore_list():
    '''
    ignore function included in the list
    '''
    # global ignore_list
    # with open(os.path.join(PLUGINDIR_PATH, "ignore.txt")) as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         e = line.strip()
    #         if e not in ignore_list:
    #             ignore_list.append(e)
    # f.close()
    return Settings().get_string_list("algoprophet.ignoreFunctionNames")


def load_inst_tag_list(bv: BinaryView, addr):
    '''
    load previous tag list from bndb
    '''
    # global inst_tag_list
    inst_tag_list = {}
    tags = bv.get_user_data_tags_at(addr)
    if len(tags) != 0:
        if addr not in inst_tag_list:
            inst_tag_list[addr] = list()
        for tag in tags:
            inst_tag_list[addr].append(tag.data)
    return inst_tag_list


def add_model_tag_to_inst(bv: BinaryView, addr, model, user_tag):
    '''
    add tag to instruction if model still not identified
    '''
    # global inst_tag_list
    inst_tag_list = load_inst_tag_list(bv, addr)
    if addr not in inst_tag_list:
        inst_tag_list[addr] = list()
    if model in inst_tag_list[addr]:
        return
    inst_tag_list[addr].append(model)
    bv.create_user_data_tag(addr, user_tag, f'{model}')


def matcher(bv: BinaryView, f_dfg: nx.DiGraph, f: Function, user_tag: TagType):
    for matched_model, matched_inst_dest in graph_match.match(f_dfg).items():
        if len(matched_inst_dest) != 0:
            print('info', "AlgoProphet: Find ", matched_model, " in ", f.name)
            for idx in matched_inst_dest[0]:
                address = f.mlil.ssa_form[idx].address
                print("address: ", hex(address))
                add_model_tag_to_inst(bv, address, matched_model, user_tag)
                '''
                rename variable only if matched instruction is MediumLevelILSetVarSsa
                e.g., called function is blackbox so we won't rename variable
                '''
                s = f.mlil.ssa_form[idx]
                if isinstance(s, MediumLevelILSetVarSsa):
                    target_var = s.dest.var
                    name = target_var.name
                    split = name.split('_')
                    if split and (split[0] == 'var' or split[0] in f.arch.regs):
                        if check := [s for s in split[1:] if not re.match(r'[0-9]+', s)]:
                            print('debug', f'{s.address:#x} ({s}): not renaming var {name!r} ({split = }) ({check = })')
                            print('warn', f'Not renaming non-default named var {name!r} at {s.address:#x}.\nTo have AlgoProphet rename this variable, unset its name and rerun Match Algos')
                            continue
                    target_var.set_name_async(matched_inst_dest[1])
                    target_var.function.view.update_analysis()


def function_iterator(bv: BinaryView):
    '''
    iterate all functions from binary and match models
    '''
    # dfg for all functions in current binary
    print(bv)
    # create user tag if not exist
    if bv.get_tag_type("AlgoProphet") is None:
        bv.create_tag_type("AlgoProphet", chr(0x2140))
    tag = bv.get_tag_type("AlgoProphet")
    ignore_list = get_ignore_list()
    for f in bv.functions:
        if (f.name in ignore_list) or (not f.name[0].isalpha()):
            continue
        matcher(bv, dfg.read_binaryview(bv, f.mlil), f, tag)
        dfg.clean_data()


def check_context(ctx: UIActionContext, action: str, require_function: bool = True) -> bool:
    if not (ctx and ctx.context and ctx.binaryView):
        log_error(f"AlgoProphet - {action}: no binary view selected")
        return False
    if require_function and not (ctx and ctx.function and ctx.address):
        log_error(f"AlgoProphet - {action}: no function selected")
        return False
    return True


def match_helper(ctx: UIActionContext):
    if check_context(ctx, 'Match Algos', require_function=False):
        function_iterator(ctx.binaryView)


def rk_match_helper(bv: BinaryView, func: Function):
    # create user tag if not exist
    if bv.get_tag_type("AlgoProphet") is None:
        bv.create_tag_type("AlgoProphet", chr(0x2140))
    tag = bv.get_tag_type("AlgoProphet")
    if func.name in get_ignore_list():
        return
    matcher(bv, dfg.read_binaryview(bv, func.mlil), func, tag)
    dfg.clean_data()


def adjust_helper(ctx: UIActionContext):
    if not check_context(ctx, 'Adjust Tested models'):
        return
    bv = ctx.binaryView
    func_name = TextLineField("Specify the function name")
    func_name.text = ctx.function.name
    var_list = MultilineTextField("Ignore variable names")
    constant_list = MultilineTextField("Ignore constants")
    misc_list = MultilineTextField("Ignore based on labels")
    get_form_input([func_name, var_list, constant_list, misc_list], "AlgoProphet")
    f = bv.get_functions_by_name(func_name.result)[0]
    print("Adjust current model on function: ", f.name)
    filter_dict = dict()
    filter_dict["var_list"] = list()
    for i in var_list.result.split("\n"):
        i = i.strip()
        if len(i) != 0:
            filter_dict["var_list"].append(i)
    filter_dict["constant_list"] = list()
    for i in constant_list.result.split("\n"):
        i = i.strip()
        if len(i) != 0:
            filter_dict["constant_list"].append(i)
    filter_dict["misc_list"] = list()
    for i in misc_list.result.split("\n"):
        i = i.strip()
        if len(i) != 0:
            filter_dict["misc_list"].append(i)
    dfg_processor.read_dfg_with_fdict(f.name, filter_dict)


def rk_adjust_helper(bv: BinaryView, func: Function):
    uc = UIContext.activeContext()
    # cv = uc.getCurrentView()
    # hts = cv.getHighlightTokenState()
    ah = uc.getCurrentActionHandler()
    ctx = ah.actionContext()

    h = ctx.token
    f = ctx.function.name
    token_name = h.token.text
    # token_type = h.token.type
    dfg_processor.rk_read_dfg(f, token_name, False)


def rkop_adjust_helper(bv: BinaryView, instr: MediumLevelILInstruction):
    uc = UIContext.activeContext()
    # cv = uc.getCurrentView()
    # hts = cv.getHighlightTokenState()
    ah = uc.getCurrentActionHandler()
    ctx = ah.actionContext()

    h = ctx.token
    f = ctx.function.name
    token_name = h.token.text
    # token_var = h.localVar
    dfg_processor.rk_read_dfg(f, token_name, True)


def pre_process(subject: Union[Subject, List[Subject]]) -> SelectionState:
    function = block = instruction = None
    blocks = list()
    instructions = list()
    match subject:
        case [*subjects]:
            for s in subjects:
                ms = pre_process(s)
                assert function is None or ms.function == function
                function = ms.function
                instructions.extend(ms.instructions)
                blocks.extend(ms.blocks)
        case Function(hlil=hlil):
            return pre_process(hlil)
        case MediumLevelILFunction(
            il_form=FunctionGraphType.MediumLevelILFunctionGraph, ssa_form=ssa_form
        ):
            return pre_process(ssa_form)
        case MediumLevelILFunction(
            il_form=FunctionGraphType.MediumLevelILSSAFormFunctionGraph
        ):
            function = subject.ssa_form
            instructions = list(function.instructions)
            blocks = list(function.basic_blocks)
        case MediumLevelILInstruction(function=il_function):
            if subject.ssa_form != subject:
                instructions = [
                    i
                    for i in il_function.ssa_form.instructions
                    if i.non_ssa_form == subject
                ]
                return pre_process(instructions)
            function = il_function.ssa_form
            instruction = subject.ssa_form
            block = instruction.il_basic_block
            instructions = [instruction]
            blocks = [block]
        case MediumLevelILBasicBlock(il_function=il_function):
            function = il_function.ssa_form
            block = subject
            blocks = [block]
            instructions = list(block)
        case object(source_function=source_function):
            return pre_process(source_function)
        case _:
            raise ValueError(f"Unrecognized subject type: {type(subject)}")
    return SelectionState(
        function,
        blocks,
        instructions,
    )


def selection_helper(bv: BinaryView, start: int, end: int) -> None:
    try:
        funcs = list()
        instructions = list()
        addr = start
        length = end - addr
        if length <= bv.get_instruction_length(start):
            f = bv.get_function_at(start)
            if f:
                funcs.append(f)
                instructions = [i for i in f.mlil.instructions]
        # if there are no functions or instructions chosen
        if not funcs or not instructions:
            # check whether this is valid address
            while addr < end and bv.is_offset_code_semantics(addr):
                new_addr = addr + 1
                for f in bv.get_functions_containing(addr):
                    if f not in funcs:
                        funcs.append(f)
                        new_addr = max(new_addr, f.highest_address)
                addr = new_addr
            for f in funcs:
                if start > f.lowest_address or f.highest_address >= end:
                    # in this case, we will only take part of func instructions
                    for i in f.mlil.instructions:
                        if start <= i.address < end and i not in instructions:
                            instructions.append(i)
                else:
                    # otherwise, we would take whole func instructions
                    for i in f.mlil.instructions:
                        if i not in instructions:
                            instructions.append(i)
        ms = pre_process(instructions)

        filter_dict = dict()
        filter_dict["instr_list"] = list()
        mlil_idx = [i.instr_index for i in ms.instructions]
        filter_dict["instr_list"].extend(mlil_idx)

        dfg.read_binaryview(bv, ms.function, filter_dict)
        dfg.clean_data()
    except:
        log_error(traceback.format_exc())


def build_helper(ctx: UIActionContext):
    if check_context(ctx, 'Build a model'):
        selection_helper(ctx.binaryView, ctx.address, ctx.address + ctx.length)


def rk_build_helper(bv, start, length):
    selection_helper(bv, start, start + length)


UIAction.registerAction("AlgoProphet - Match Algos")
UIAction.registerAction("AlgoProphet - Adjust Tested models")
UIAction.registerAction("AlgoProphet - Build a model")
UIActionHandler.globalActions().bindAction("AlgoProphet - Match Algos", UIAction(match_helper))
UIActionHandler.globalActions().bindAction("AlgoProphet - Build a model", UIAction(build_helper))
UIActionHandler.globalActions().bindAction("AlgoProphet - Adjust Tested models", UIAction(adjust_helper))

PluginCommand.register_for_function(
    "AlgoProphet\\Match Algos", "Match current function with existing models", rk_match_helper
)
PluginCommand.register_for_range(
    "AlgoProphet\\Build a model", "Build DFG model based on specified instructions", rk_build_helper
)
PluginCommand.register_for_function(
    "AlgoProphet\\Adjust a model\\SSAVars or Constants", "Adjust the model for current function", rk_adjust_helper
)
PluginCommand.register_for_medium_level_il_instruction(
    "AlgoProphet\\Adjust a model\\Operations", "Adjust the model for current fuinction", rkop_adjust_helper
)
