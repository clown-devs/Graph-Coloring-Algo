import argparse

from src.drawer import *
from src.generator import *
from src.algo.greedy import *

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-v", help="vertices count", type=int)
    args = argParser.parse_args()

    n = args.v
    
    if n is None:
        n = 10
    
    g = generate_graph(n)

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


if __name__ == "__main__":
    main()