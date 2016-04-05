from graph import *
from algorithms import DijkstraAlgorithm

g = Graph()

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

g.add_edge(node_1, node_2, length=1)
g.add_edge(node_2, node_3, length=2)
g.add_edge(node_1, node_3, length=4)

distance, path = DijkstraAlgorithm.get_path(g, node_1, node_3)
assert(distance == 3)
