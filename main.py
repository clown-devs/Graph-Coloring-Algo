from src.models import *
from src.drawer import *
from src.generator import *
g = generate_graph(10)
vertecies = g.getVertices()
print(vertecies[0].getAdjecentVertices())
d = Drawer(g)
d.draw('graph.html')






