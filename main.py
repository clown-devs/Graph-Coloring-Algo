from src.models import *
from src.drawer import *
from src.generator import *
g = generate_graph(10)

d = Drawer(g)
d.draw('graph.html')






