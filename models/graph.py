

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # {Vertex-id : Vertex}

    def addNeighbor(self, vertex):
        self.connectedTo[vertex.id] = vertex

    def __str__(self):
        return str(self.id)

    def isConnectedTo(self, vertex_id):
        return vertex_id in self.connectedTo
    
    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertList = {} # {Vertex-id : Vertex}  

    def addVertex(self, vertex):
        self.vertList[vertex.id] = vertex

    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.vertList:
            self.addVertex(vertex1)
        if vertex2 not in self.vertList:
            self.addVertex(vertex2)
        self.vertList[vertex1.id].addNeighbor(vertex2)
        self.vertList[vertex2.id].addNeighbor(vertex1)
        
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()