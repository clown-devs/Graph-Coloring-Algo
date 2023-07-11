from src.drawer import *
from src.generator import *
from src.algo.greedy import *

g = generate_graph(100)

color_number_greedy = greedy_coloring(g) 
g.resetColors()
color_number_sorting_greedy = sorting_greedy_coloring(g)

print("-------------------")
print("Color numbers for this graph:")
print(" Greedy:", color_number_greedy)
print(" Greedy (sorting heuristic):", color_number_sorting_greedy)
print("-------------------")
d = Drawer(g)
d.draw('graph.html')
