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
class GraphDrawer:

    def __init__(self):
        self.G = nx.Graph()
        self.initialNode = ''
        self.path = []
        
    def loadEdgeList(self,edgeList):
        for edge in edgeList:
            self.G.add_edge(edge[0], edge[1], weight = edge[2], length = edge[2])
    
    def chooseIntitial(self, node):
        self.initialNode = node
 
    def choosePath(self, path):
        self.path = path

    def plot(self):
        pos = nx.spring_layout(self.G) # different layout?

        # draw nodes
        nx.draw_networkx_nodes(self.G,pos, nodelist = [x for x in self.G.nodes() if not x == self.initialNode], node_color = 'b', node_size=3500)
        nx.draw_networkx_nodes(self.G,pos, nodelist = [self.initialNode], node_color = 'r', node_size=3500)

        # draw edges
        nx.draw_networkx_edges(self.G, pos, edgelist = [x for x in self.G.edges() if not x in self.path], width=1)
        nx.draw_networkx_edges(self.G, pos, edgelist = self.path, width=1, edge_color = 'r')

        # draw labels
        nx.draw_networkx_labels(self.G, pos)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels = labels)

        plt.axis('off')
        plt.savefig("hihi.png")
        plt.show()

# usage example
a = GraphDrawer()
a.loadEdgeList([('Da Nang', 'Sai Gon', 5),('Da Nang', 'Hue', 2),('Can Tho', 'Hue', 6),('Long An', 'Sai Gon', 1),('Ha Noi', 'Hue', 12)])
a.chooseIntitial('Long An')
a.choosePath([('Long An', 'Sai Gon'),('Sai Gon', 'Da Nang')])
a.plot()
        
