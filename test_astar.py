import math

from graph import *
from algorithms import *

def distance(a, b):
    return math.sqrt((a.data['lat'] - b.data['lat']) ** 2 + (a.data['lng'] - b.data['lng']) ** 2)

g = Graph()

nodes = [Node(1, lat=-1, lng=-1), Node(2, lat=2, lng=3), Node(3, lat=2, lng=0)]
for node_u in nodes:
    for node_v in nodes:
        if node_u is not node_v:
            g.add_edge(node_u, node_v, length=distance(node_u, node_v))

distance, path = AstarAlgorithm.get_path(g, nodes[0], nodes[2], distance)
print distance
