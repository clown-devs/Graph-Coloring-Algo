import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.algo.greedy import *
from src.drawer import *


class Executor:
    def __init__(self, g):
        self.__g = g

    def run(self):
        g = self.__g
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