import os, json
import networkx as nx
from networkx.algorithms import isomorphism

try:
    from . import print
except:
    pass

PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))


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
            if n1["value"] == n2["value"]:
                return True
            else:
                # print("Mismatched nodes: ", n1, ", ", n2)
                return False
    else:
        # print("Mismatched nodes: ", n1, ", ", n2)
        return False


def match(target):
    formula = dict()
    with open(os.path.join(PLUGINDIR_PATH, "formula.json")) as f:
        formula = json.load(f)

    models = dict()
    for model_gml in os.listdir(os.path.join(PLUGINDIR_PATH, "models")):
        if model_gml.split(".")[-1] == "gml":
            models[formula[model_gml][0]] = list()
            models[formula[model_gml][0]].append(
                nx.read_gml(os.path.join(PLUGINDIR_PATH, "models", model_gml))
            )
            models[formula[model_gml][0]].append(formula[model_gml][1])

    matched_result = dict()

    for model_name, model in models.items():
        # graph matcher
        gm = isomorphism.DiGraphMatcher(target, model[0], node_match=node_match)
        if gm.subgraph_is_isomorphic() == True:
            for matched_list in list(gm.subgraph_isomorphisms_iter()):
                sg = list()
                for node in matched_list:
                    sg.append(node)
                graph_ = target.copy().subgraph(sg)
                inst_list = list()
                for src, dst, data in graph_.edges(data=True):
                    if "idx" in data and data["idx"] not in inst_list:
                        if data["idx"] not in inst_list:
                            inst_list.append(data["idx"])
                matched_result[model_name] = list()
                matched_result[model_name].append(inst_list)
                matched_result[model_name].append(model[1])

    for model_name, matched_data in matched_result.items():
        print(f"model name: {model_name}")
        print(f"instr: {matched_data[0]}")
        print(f"dest: {matched_data[1]}")

    return matched_result
