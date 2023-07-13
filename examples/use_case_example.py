import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executor import *
from src.models import *

vertices = [Vertex(i) for i in range(10)]
g = Graph()

for v in vertices[1:]: g.addVertex(v)
g.addEdge(vertices[1].id, vertices[2].id)
g.addEdge(vertices[1].id, vertices[3].id)
g.addEdge(vertices[1].id, vertices[4].id)
g.addEdge(vertices[1].id, vertices[5].id)
g.addEdge(vertices[1].id, vertices[6].id)
g.addEdge(vertices[1].id, vertices[7].id)
g.addEdge(vertices[1].id, vertices[8].id)
g.addEdge(vertices[1].id, vertices[9].id)

executor = Executor(g)
executor.run()