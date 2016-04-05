from graph_drawer import GraphDrawer

# usage example
a = GraphDrawer()
a.loadEdgeList([('Da Nang', 'Sai Gon', 5),('Da Nang', 'Hue', 2),('Can Tho', 'Hue', 6),('Long An', 'Sai Gon', 1),('Ha Noi', 'Hue', 12)])
a.chooseIntitial('Long An')
a.choosePath([('Long An', 'Sai Gon'),('Sai Gon', 'Da Nang')])
a.plot()