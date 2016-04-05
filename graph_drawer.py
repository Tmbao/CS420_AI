try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
import pygraphviz as pg

'''
class GraphDrawer:

    def __init__(self):
        self.G = pg.AGraph()
        
    def loadEdgeList(self,edgeList):
        for edge in edgeList:
            self.G.add_edge(edge[0], edge[1], weight = edge[2], length = edge[2])
            
    def plot(self):
        self.G.draw('hihi.png', format='png', prog='neato')
'''

def plot(file_name, graph, source, target, path, weight_tag='weight', name_tag='name', color='r'):
    pos = nx.spring_layout(graph) # different layout?

    # draw nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=[x for x in graph.nodes() if not x == source])
    nx.draw_networkx_nodes(graph, pos, nodelist=[source], node_color=color)

    # draw edges
    nx.draw_networkx_edges(graph, pos, edgelist=[x for x in graph.edges() if not x in path])
    nx.draw_networkx_edges(graph, pos, edgelist=path, width=1, edge_color=color)

    # draw labels
    node_labels = nx.get_node_attributes(graph, name_tag)
    nx.draw_networkx_labels(graph, pos, labels=node_labels)
    labels = nx.get_edge_attributes(graph, weight_tag)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.axis('off')
    plt.savefig(file_name)
    plt.show()
        
