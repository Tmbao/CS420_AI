

class Node(object):
    def __init__(self, label, **kwargs):
        self.label = label
        self.data = kwargs

    def __cmp__(self, other):
        return __cmp__(self.label, other.label)


class Edge(object):
    LENGTH_TAG = 'length'
    def __init__(self, source, target, **kwargs):
        self.source = source
        self.target = target
        self.data = kwargs


class Graph(object):
    """
    Graph class
    """

    # Data
    adjacency_nodes = {}

    def __init__(self):
        self.adjacency_nodes = {}

    def add_node(self, node_u):
        if node_u not in self.adjacency_nodes:
            self.adjacency_nodes[node_u] = set()

    def add_directed_edge(self, node_u, node_v, **kwargs):
        # Check if our graph contains the two nodes 
        self.add_node(node_u)
        self.add_node(node_v)

        # Add edge into graph
        self.adjacency_nodes[node_u].add(Edge(node_u, node_v, **kwargs))


    def add_edge(self, node_u, node_v, **kwargs):
        self.add_directed_edge(node_u, node_v, **kwargs)
        self.add_directed_edge(node_v, node_u, **kwargs)

