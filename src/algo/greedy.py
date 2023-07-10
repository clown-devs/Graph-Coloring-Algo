from ..models import *
from random import *


# returns the number of colors used
#TODO: Colors generator
def greedy(g: Graph, strategy: callable) -> int:
    vertices = strategy(g)
    if len(vertices) == 0:
        return 0
    
    
    colors = ['#0000FF', '#00FF00', '#FF0000', '0F0F0F', '#FFFF00', '#00FFFF', '#FF00FF', '#FFFFFF']
    max_color = 0
    
    for vertex in vertices:
        adjecent_colors = []
        for adjecentVertex in vertex.getAdjecentVertices():
            adjecent_colors.append(adjecentVertex.color)
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
        
        
