from .models import *
import random
def generate_graph(n):
    g = Graph()
    for i in range(1, n + 1):
        g.addVertex(Vertex(i))
    for i in range(1, n):
        g.addEdge(g.getVertex(i).id, g.getVertex(i + 1).id)

    for i in range(1, random.randint(1,n)):
        a = b = 1
        while(a == b): # To remove self loops
            a = random.randint(1,n)
            b = random.randint(1,n)
        g.addEdge(g.getVertex(a).id, g.getVertex(b).id)
    return g