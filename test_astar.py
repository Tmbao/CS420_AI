import math
import networkx as nx

from graph_algorithms import *

g = nx.Graph()
g.add_node(0, lat=-1, lng=-1)
g.add_node(1, lat=2, lng=3)
g.add_node(2, lat=2, lng=0)

attr_lat = nx.get_node_attributes(g, 'lat')
attr_lng = nx.get_node_attributes(g, 'lng')

def heuristic_func(cur_node, target):
	return math.sqrt((attr_lat[cur_node] - attr_lat[target]) ** 2 + (attr_lng[cur_node] - attr_lng[target]) ** 2)

for node_u in range(3):
	for node_v in range(node_u + 1, 3):
            g.add_edge(node_u, node_v, weight=heuristic_func(node_u, node_v))

algo = AstarAlgorithm(heuristic_func=heuristic_func)
distance, path = algo.get_path(g, 0, 2)
print distance
print path