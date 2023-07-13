from src.models import Graph, Vertex
from src.algo.RLF import RLF
from src.generator import *
from src.drawer import Drawer


def wheel_example():
    graph = generate_wheel_graph(10)
    color_number = RLF(graph)
    print("Color number(RLF):", color_number)
    drawer = Drawer(graph)
    drawer.draw('graph.html')
