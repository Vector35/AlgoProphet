import sys
import networkx as nx
import matplotlib.pyplot as plt

# this test is used for the graph which include load operation

graph = nx.read_gml(sys.argv[1])
option = sys.argv[2]
graph_ = graph.copy()

load_nodes = list()

# node = (name, attr)
for (name, attr) in graph.nodes(data=True):
    if attr["value"] == "load":
        load_nodes.append(name)

subgraph_cores = list()

# break all out_edges from all load nodes in the graph
for node in load_nodes:
    for out_edge in graph_.out_edges(node):
        subgraph_cores.append(out_edge[1])
        graph.remove_edge(node, out_edge[1])

for load_node in load_nodes:        
    subgraph_cores.append(load_node)

subgraph_nodes = list()
graph = graph.to_undirected()
for core in subgraph_cores:
    nodes = list(nx.shortest_path(graph, core).keys())
    print(nodes)
    subgraph_nodes.append(nodes)

subgraph = list()
for subgraph_list in subgraph_nodes:
    subgraph.append(graph_.subgraph(subgraph_list))

# test results
# test0
# test1
# test2 shows how array element indexed
if option == "bb":
    # this is bb-based
    for i in range(len(subgraph)):
        print(subgraph[i].nodes)
        nx.write_gml(subgraph[i], "./sepmodel/test" + str(i) + ".gml")
        nx.draw(subgraph[i], with_labels = True)
        plt.savefig("./sepmodel/test" + str(i) + ".png")
        # clean the old graph
        plt.clf()
elif option == "f":
    # this is function-based
    for i in range(len(subgraph)):
        print(subgraph[i].nodes)
        nx.write_gml(subgraph[i], "./sepmodel/function-based/test" + str(i) + ".gml")
        nx.draw(subgraph[i], with_labels = True)
        plt.savefig("./sepmodel/function-based/test" + str(i) + ".png")
        # clean the old graph
        plt.clf()