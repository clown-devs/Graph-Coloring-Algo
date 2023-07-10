from src.models.graph import *
from src.view.drawer import *

g = Graph()
g.addVertex(Vertex(1, '#FF0000'))
g.addVertex(Vertex(2, '#00FF00'))
g.addVertex(Vertex(3, '#0000FF'))
g.addEdge(g.getVertex(1), g.getVertex(2))
g.addEdge(g.getVertex(2), g.getVertex(3))

d = Drawer(g)
d.draw('graph.html')






