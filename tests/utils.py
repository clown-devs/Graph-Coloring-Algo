import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.models import *

def is_corrected_colored(g: Graph) -> bool:
    for vertex in g.getVertices():
        for adjecent_vertex in vertex.getAdjecentVertices():
            if vertex.colorId == adjecent_vertex.colorId:
                return False
    return True