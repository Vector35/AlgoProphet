import sys
import networkx as nx
import matplotlib.pyplot as plt

func = sys.argv[1]
graph = nx.read_gml(func)
nx.draw(graph, with_labels=True)
plt.savefig(func + ".png")