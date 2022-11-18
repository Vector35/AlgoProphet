import os
import networkx as nx

try:
    import matplotlib.pyplot as plt
except:
    plt = None

from . import print, log_warn

PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))


def adjust_dfg(func_name, dfgraph, filter_dict):
    remove_node_list = list()
    for i in filter_dict["var_list"]:
        for x, y in dfgraph.nodes(data=True):
            if (i in y["value"]) and (x not in remove_node_list):
                remove_node_list.append(x)
    for i in filter_dict["constant_list"]:
        for x, y in dfgraph.nodes(data=True):
            if (i == y["value"]) and (x not in remove_node_list):
                remove_node_list.append(x)
    for i in filter_dict["misc_list"]:
        for x, y in dfgraph.nodes(data=True):
            if (i == x) and (x not in remove_node_list):
                remove_node_list.append(x)
    # iterate remove_node_list on dfgraph
    for n in remove_node_list:
        dfgraph.remove_node(n)
    nx.draw(dfgraph, with_labels=True)
    if plt is not None:
        plt.savefig(os.path.join(PLUGINDIR_PATH, "test", func_name + ".png"))
    nx.write_gml(dfgraph, os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml"))
    if plt is not None:
        plt.clf()


def read_dfg_with_fdict(func_name, filter_dict):
    gml_name = os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml")
    png_name = os.path.join(PLUGINDIR_PATH, "test", func_name + ".png")
    if os.path.exists(gml_name) is False:
        log_warn("Model not exists, please check test folder")
        return
    dfgraph = nx.read_gml(gml_name)
    # delete file after read
    os.remove(gml_name)
    os.remove(png_name)
    adjust_dfg(func_name, dfgraph, filter_dict)


def rk_get_op(dfgraph, label):
    if dfgraph.nodes[label]["type"] == "operation":
        return label
    e = dfgraph.out_edges(label)
    print(type(e))
    print(e)
    if len(e) == 0:
        return None
    return rk_get_op(dfgraph, list(e)[0][1])


def rk_read_dfg(func_name, label, rm_op):
    gml_name = os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml")
    png_name = os.path.join(PLUGINDIR_PATH, "test", func_name + ".png")
    if os.path.exists(gml_name) is False:
        log_warn("Model not exists, please check test folder")
        return
    dfgraph = nx.read_gml(gml_name)
    if not dfgraph.has_node(label):
        log_warn(f"Cannot find node {label}")
        return
    if rm_op is True:
        # this is used for removing operation nodes
        closest_op = rk_get_op(dfgraph, label)
        if closest_op is None:
            log_warn(f"Cannot find related operation nodes for {label}")
            return
        label = closest_op
    # remove nodes from graph
    dfgraph.remove_node(label)
    nx.draw(dfgraph, with_labels=True)
    # delete file after read
    os.remove(gml_name)
    os.remove(png_name)
    if plt is not None:
        plt.savefig(os.path.join(PLUGINDIR_PATH, "test", func_name + ".png"))
    nx.write_gml(dfgraph, os.path.join(PLUGINDIR_PATH, "test", func_name + ".gml"))
    if plt is not None:
        plt.clf()
