import math
import networkx as nx

from graph_algorithms import *
import graph_drawer

def read_entire_file(file_name):
	with open(file_name, 'r') as file:
		content = file.read()
	return content.split()

tokens = read_entire_file('demo_map.txt')
token_id = -1

def next_token():
	global token_id
	global tokens

	token_id += 1
	if token_id < len(tokens):
		return tokens[token_id]
	else:
		return None


graph = nx.Graph()

# add nodes
n_nodes = int(next_token())
for i in range(n_nodes):
	node_id = int(next_token())
	node_name = next_token()
	node_lat = int(next_token())
	node_lng = int(next_token())

	graph.add_node(node_id, name=node_name, lat=node_lat, lng=node_lng)


# add edges
n_edges = int(next_token())
for i in range(n_edges):
	u = int(next_token())
	v = int(next_token())
	c = int(next_token())

	graph.add_edge(u, v, weight=c)

source = int(next_token())
target = int(next_token())


attr_lat = nx.get_node_attributes(graph, 'lat')
attr_lng = nx.get_node_attributes(graph, 'lng')
attr_name = nx.get_node_attributes(graph, 'name')

def heuristic_func(cur_node, target):
	return math.sqrt((attr_lat[cur_node] - attr_lat[target]) ** 2 + (attr_lng[cur_node] - attr_lng[target]) ** 2)

algo = AstarAlgorithm(heuristic_func=heuristic_func)
distance, path = algo.get_path(graph, source, target)
print distance
print path
graph_drawer.plot('demo.png', graph, source, target, path)
