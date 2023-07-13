from ..models import *
from typing import Tuple
from copy import deepcopy

def get_max_neighbours_vertex(g: Graph) -> Vertex|None:
    max = -1
    max_vertex = None
    for vertex in g.getVertices():
        if len(vertex.getAdjecentVertices()) > max:
            max = len(vertex.getAdjecentVertices())
            max_vertex = vertex
    return max_vertex

def not_adjecent_to_all(vertex: Vertex, S: list[Vertex]) -> bool:
    for s in S:
        if vertex.isConnectedTo(s.getId()) or vertex.getId() == s.getId():
            return False
    return True

def neighbours_adjecent_to_s(vertex: Vertex, S: list[Vertex]) -> int:
    count = 0
    for neighbours in vertex.getAdjecentVertices():
        for s in S:
            if neighbours.isConnectedTo(s.getId()):
                count += 1
                break
    return count


# Minimum neighbours that is not adjecent to S
def get_winner(candidates: list[Vertex], S: list[Vertex]) -> Vertex:
    min = None
    min_vertex = None
    for vertex in candidates[1]:
        #count = len(vertex.getAdje neighbours_adjecent_to_s(vertex, S)
        count = len(vertex.getAdjecentVertices()) - neighbours_adjecent_to_s(vertex, S)
        if min is None or count < min:
            min = count
            min_vertex = vertex
    return min_vertex

def recalculate_candidates(vertex: Vertex, candidates: list[int, list[Vertex]], S: list[Vertex]):
    nads = neighbours_adjecent_to_s(vertex, S)

    if nads > candidates[0]:
        candidates[0] = nads
        candidates[1] = [vertex]
        return candidates
    
    if nads == candidates[0]:
        candidates[1].append(vertex)
        return candidates
    
    return candidates
        
    
def RLF_coloring(g: Graph, S_final: list[list[Vertex]]):
    for i in range(len(S_final)):
        color = i
        for vertex in S_final[i]:
            g.getVertex(vertex.getId()).setColor(color)

  
def RLF(g : Graph) -> int:
    g_copy = deepcopy(g)
    S = []
    S_final = []
    while (len(g_copy) != 0):
        first_vertex = get_max_neighbours_vertex(g_copy)
        assert(first_vertex != None)
        S.append(first_vertex)
        while True:
            # num of neighbours that adjecent to S and candidates
            candidates = [-1, []]
            for vertex in g_copy.getVertices():
                if not_adjecent_to_all(vertex, S):
                    candidates = recalculate_candidates(vertex, candidates, S)

            if len(candidates[1]) == 0:
                    break
                
            winner = get_winner(candidates, S)
            assert(winner != None)
            S.append(winner)
        

        S_final.append(S)
        for vertex in S:
            g_copy.removeVertex(vertex.getId())
        S = []
          
    RLF_coloring(g, S_final)
    return len(S_final)