from curses import has_key
import sys
import networkx as nx
from networkx.algorithms import isomorphism

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
                    if n1["shift_width"]/n1["base_width"] == n2["shift_width"]/n2["base_width"]:
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
                #print("Mismatched nodes: ", n1, ", ", n2)
                return False
    else:
        #print("Mismatched nodes: ", n1, ", ", n2)
        return False

models = list()
for i in range(1, len(sys.argv) - 1):
    models.append(nx.read_gml(sys.argv[i]))
graph = nx.read_gml(sys.argv[-1])

for i in range(len(models)):
    model = models[i]
    print("Use model: ", sys.argv[i + 1])
    # graph matcher
    gm = isomorphism.DiGraphMatcher(graph, model, node_match=node_match)
    if gm.subgraph_is_isomorphic() == True:
        print("Matched!")
        for matched_list in list(gm.subgraph_isomorphisms_iter()):
            sg = list()
            for node in matched_list:
                sg.append(node)
            graph_ = graph.copy().subgraph(sg)
            inst_list = list()
            for src, dst, data in graph_.edges(data=True):
                if "idx" in data and data["idx"] not in inst_list:
                    if data["idx"] not in inst_list:
                        inst_list.append(data["idx"])
            if len(inst_list):
                print("Matched instructions: ", inst_list)