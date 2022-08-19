import os, sys
import networkx as nx
import matplotlib.pyplot as plt

PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))

def adjust_dfg(func_name, dfgraph, filter_dict):
    tmp = dfgraph.copy()
    for i in filter_dict["var_list"]:
        for x, y in tmp.nodes(data = True):
            if i in y["value"]:
                dfgraph.remove_node(x)
    tmp = dfgraph.copy()
    for i in filter_dict["constant_list"]:
        for x, y in tmp.nodes(data = True):
            if i == y["value"]:
                dfgraph.remove_node(x)
    nx.draw(dfgraph, with_labels=True)
    plt.savefig(os.path.join(PLUGINDIR_PATH, "test", func_name + ".png"))
    nx.write_gml(dfgraph, os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml"))

def read_dfg(func_name, filter_dict):
    dfgraph = nx.read_gml(os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml"))
    adjust_dfg(func_name, dfgraph, filter_dict)