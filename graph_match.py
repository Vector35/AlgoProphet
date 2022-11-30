from collections import defaultdict
import os
import json
import networkx as nx
from networkx.algorithms import isomorphism

from . import get_algoprophet_path, log_warn, log_debug


def node_match(n1, n2):
    if n1["type"] == n2["type"]:
        if n1["type"] == "ssavar":
            return True
        elif n1["type"] == "operation":
            if "load" in n1["value"] and "load" in n2["value"]:
                # match load nodes
                # must have base_width
                # but not necessarily have shift_width
                if "shift_width" in n1.keys() and "shift_width" in n2.keys():
                    if (
                        n1["shift_width"] / n1["base_width"]
                        == n2["shift_width"] / n2["base_width"]
                    ):
                        # print("true: ", n1, " ", n2)
                        return True
                    else:
                        # print("false: ", n1, " ", n2)
                        return False
                else:
                    return True
            elif "ADD" in n1["value"] and "ADD" in n2["value"]:
                return True
            elif "MUL" in n1["value"] and "MUL" in n2["value"]:
                return True
            elif n1["value"] == n2["value"]:
                return True
            else:
                return False
        else:
            # constant
            # TODO: implement fuzzy matching for floating point values
            # TODO: implement evaluation for python expressions (and math.* constants)
            if n1["value"] == n2["value"]:
                return True
            else:
                # print("Mismatched nodes: ", n1, ", ", n2)
                return False
    else:
        # print("Mismatched nodes: ", n1, ", ", n2)
        return False


def match(target: nx.DiGraph):
    formula_plugin_paths = [get_algoprophet_path("formula.json", plugin_only=True)]
    if (
        (formula_user_path := get_algoprophet_path("formula.json")) and
        os.path.exists(formula_user_path)
    ):
        formula_plugin_paths.append(formula_user_path)
    formula = dict()
    for formula_path in formula_plugin_paths:
        with open(formula_path) as f:
            formula.update(json.load(f))

    models = defaultdict(list)
    # for model_gml in os.listdir(get_algoprophet_path("models")):
    for model_gml in formula.keys():
        model_gml_path = get_algoprophet_path("models", model_gml, allow_default=False)
        if not model_gml_path or not os.path.exists(model_gml_path):
            model_gml_path = get_algoprophet_path("models", model_gml, plugin_only=True)
            if not os.path.exists(model_gml_path):
                log_warn(f'Model GML file not found in models folder: {model_gml}')
                continue
        # if model_gml.split(".")[-1] == "gml":
        if os.path.splitext(model_gml)[-1] == ".gml":
            models[formula[model_gml][0]].append(
                nx.read_gml(model_gml_path)
            )
            models[formula[model_gml][0]].append(formula[model_gml][1])

    matched_result = defaultdict(list)

    for model_name, model in models.items():
        # graph matcher
        gm: isomorphism.DiGraphMatcher = isomorphism.DiGraphMatcher(target, model[0], node_match=node_match)
        if gm.subgraph_is_isomorphic():
            for matched_list in gm.subgraph_isomorphisms_iter():
                target_copy: nx.DiGraph = target.copy()
                graph_: nx.DiGraph = target_copy.subgraph(sorted(list(matched_list.keys())))
                inst_list = []
                edge_view: nx.reportviews.OutEdgeView = graph_.edges(data=True)
                for src, dst, data in edge_view:
                    if "idx" in data and data["idx"] not in inst_list:
                        if data["idx"] not in inst_list:
                            inst_list.append(data["idx"])
                matched_result[model_name].append(inst_list)
                matched_result[model_name].append(model[1])

    for model_name, matched_data in matched_result.items():
        log_debug(f"Loaded model name: {model_name}")
        log_debug(f"instr: {matched_data[0]}")
        log_debug(f"dest: {matched_data[1]}")

    return matched_result
