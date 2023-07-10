from ..models import *

def sortStrategy(g: Graph) -> list:
    vertices = g.getVertices()
    vertices.sort(key=lambda v: len(v.getAdjecentVertices()), reverse=True)
    return vertices