from copy import *
from ..models import *
from functools import lru_cache

def chromaticPolynom(graphSize: int, q: int, coefs: list):
    res = 0
    for i in range(graphSize + 1):
        res += coefs[i] * (q ** i) 
    return res

def contractVertexToNew(u: Vertex, new: Vertex):
    for adjecent in u.getAdjecentVertices():
        adjecent.addNeighbor(new) 
        new.addNeighbor(adjecent)

def contract(u: Vertex, v: Vertex, g: Graph) -> Graph:
    res = deepcopy(g)
    w = Vertex(u.id)
    u = res.getVertex(u.id)
    v = res.getVertex(v.id)
    
    res.removeEdge(u, v)
    res.removeVertex(u.id)
    res.removeVertex(v.id)

    contractVertexToNew(u, w)
    contractVertexToNew(v, w)
    
    res.addVertex(w)
    return res

def delta(l1: list, l2: list):
    return [l1[i] - l2[i] for i in range(len(l1))]

@lru_cache
def P(g: Graph, n: int) -> list:
    if g.empty():
        p = [0] * n
        p[len(g.getVertices())] = 1
        return p
    
    for v in g.getVertices():
        for adjecent in v.getAdjecentVertices():
            conractG = contract(v, adjecent, g)
            deleteG = deepcopy(g)
            deleteG.removeEdge(v, adjecent)
            return delta(P(deleteG, n), P(conractG, n))
        
def contraction(g: Graph, colors: int) -> tuple:
    coefs = P(g, len(g) + 1)
    res = chromaticPolynom(len(g), colors, coefs)
    chromaticN = chromaticNumber(len(g), coefs) 
    return res, chromaticN

def chromaticNumber(graphSize: int, coefs: list) -> int:
    for m in range(graphSize + 1):
        if chromaticPolynom(graphSize, m, coefs) > 0:
            return m