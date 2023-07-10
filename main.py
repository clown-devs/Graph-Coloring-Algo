from src.models import *
from src.drawer import *
from src.generator import *
from src.algo.greedy import *
from src.algo.sort_greedy_strategy import *

g = generate_graph(10)

# color_number = greedy(g, lambda t: t.getVertices()) # default strategy
color_number = greedy(g, strategy=sortStrategy)

print("Color number for this graph:", color_number)
d = Drawer(g)
d.draw('graph.html')
