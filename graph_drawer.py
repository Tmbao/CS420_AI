try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx
#import pygraphviz as pg
from networkx.drawing.nx_agraph import graphviz_layout
import webbrowser

'''
!!!TODO:
Choose a good looking layout prog
http://www.graphviz.org/
'''

def plot(file_name, graph, source, target, path, weight_tag='len', name_tag='name', color='b', layout_type='neato', _figsize=(20, 20), _nodesize=4000, edge_width=2.0):
    plt.figure(figsize=_figsize)
    node_path = list(set([_node for _edge in path for _node in _edge]))
    #print node_path
    pos = graphviz_layout(graph, prog=layout_type) # choose a better prog?

    # draw nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=[x for x in graph.nodes() if not x in node_path], node_size=_nodesize)
    nx.draw_networkx_nodes(graph, pos, nodelist=node_path, node_color=color, node_size=_nodesize)

    # draw edges
    nx.draw_networkx_edges(graph, pos, edgelist=[x for x in graph.edges() if not x in path],width=edge_width)
    nx.draw_networkx_edges(graph, pos, edgelist=path, edge_color=color,width=edge_width)

    # draw labels
    node_labels = nx.get_node_attributes(graph, name_tag)
    nx.draw_networkx_labels(graph, pos, labels=node_labels)
    labels = nx.get_edge_attributes(graph, weight_tag)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.axis('off')
    plt.savefig(file_name)
    webbrowser.open(file_name)
    #plt.show()
        
