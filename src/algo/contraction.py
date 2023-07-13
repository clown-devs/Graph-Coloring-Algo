from copy import *
from ..models import *

def chromaticPolynom(g: Graph, q: int, coefs: list):
    res = 0
    for i in range(len(g.getVertices()) + 1):
        res += coefs[i] * (q ** i)
    return res

def contractVertexToNew(u: Vertex, new: Vertex):
    for adjecent in u.getAdjecentVertices():
        adjecent.removeNeighbor(u.id)
        adjecent.addNeighbor(new) 
        new.addNeighbor(adjecent)

def contract(u: Vertex, v: Vertex, g: Graph) -> Graph:
    res = deepcopy(g)
    w = Vertex(u.id)
    contractVertexToNew(u, w)
    contractVertexToNew(v, w)
    res.removeVertex(u)
    res.removeVertex(v)
    return res

def delta(l1: list, l2: list):
    return [l1[i] - l2[i] for i in range(len(l1) + 1)]

def contraction(g: Graph, n: int) -> list:
    if g.empty():
        return [0] * n + [1]
    
    for v in g.getVertices():
        for adjecent in v.getAdjecentVertices():
            conractG = contract(v, adjecent, g)
            deleteG = deepcopy(g).removeEdge(v, adjecent)
            return delta(contraction(conractG, n), contraction(deleteG, n))