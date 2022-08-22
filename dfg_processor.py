import os, sys
import networkx as nx
import matplotlib.pyplot as plt

PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))

def adjust_dfg(func_name, dfgraph, filter_dict):
    remove_node_list = list()
    for i in filter_dict["var_list"]:
        for x, y in dfgraph.nodes(data = True):
            if (i in y["value"]) and (x not in remove_node_list):
                remove_node_list.append(x)
    for i in filter_dict["constant_list"]:
        for x, y in dfgraph.nodes(data = True):
            if (i == y["value"]) and (x not in remove_node_list):
                remove_node_list.append(x)
    for i in filter_dict["misc_list"]:
        for x, y in dfgraph.nodes(data = True):
            if (i == x) and (x not in remove_node_list):
                remove_node_list.append(x)
    # iterate remove_node_list on dfgraph
    for n in remove_node_list:
        dfgraph.remove_node(n)
    nx.draw(dfgraph, with_labels=True)
    plt.savefig(os.path.join(PLUGINDIR_PATH, "test", func_name + ".png"))
    nx.write_gml(dfgraph, os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml"))
    plt.clf()

def read_dfg(func_name, filter_dict):
    gml_name = os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml")
    png_name = os.path.join(PLUGINDIR_PATH, "test", func_name + ".png")
    if os.path.exists(gml_name) == False:
        print("Model not exists, please check test folder")
        return
    dfgraph = nx.read_gml(gml_name)
    # delete file after read
    os.remove(gml_name)
    os.remove(png_name)
    adjust_dfg(func_name, dfgraph, filter_dict)