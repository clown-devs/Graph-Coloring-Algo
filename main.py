from src.models import *
from src.drawer import *
from src.generator import *
from src.algo.greedy import *

g = generate_graph(20)

color_number = greedy(g)
print("Color number for this graph:", color_number)
d = Drawer(g)
d.draw('graph.html')
