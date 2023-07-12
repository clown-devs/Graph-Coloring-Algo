from ..models import *
from random import *


def greedy_coloring(g: Graph) -> int:
    return __greedy(g.getVertices())


def sorting_greedy_coloring(g : Graph) -> int:
    vertices = g.getVertices()
    vertices.sort(key=lambda v: len(v.getAdjecentVertices()), reverse=True)
    return __greedy(vertices)


# returns the number of colors used
def __greedy(vertices: list[Vertex]) -> int:
    if len(vertices) == 0:
        return 0
    
    colors = [i for i in range(1, len(vertices) + 1)]
    max_color = 0
    
    for vertex in vertices:
        adjecent_colors = []
        for adjecentVertex in vertex.getAdjecentVertices():
            adjecent_colors.append(adjecentVertex.colorId)
        for i in range(len(colors)):
            temp_flag = False
            if colors[i] not in adjecent_colors:
                vertex.setColor(colors[i])
                temp_flag = True
                if i > max_color:
                    max_color = i
                break
        if not temp_flag:
            raise Exception("Not enough colors FIXME")
    return max_color + 1