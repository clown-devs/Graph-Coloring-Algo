from .models import *
import random
def generate_graph(n):
    g = Graph()
    for i in range(1, n + 1):
        g.addVertex(Vertex(i, '#000000'))
    for i in range(1, n):
        g.addEdge(g.getVertex(i), g.getVertex(i + 1))

    for i in range(1, random.randint(1,n/3)):
        a = b = 1
        while(a == b): # To remove self loops
            a = random.randint(1,n)
            b = random.randint(1,n)
        g.addEdge(g.getVertex(a), g.getVertex(b))
    return g