class Vertex:
    def __init__(self, key, colorId=None):
        self.id = key
        self.colorId = colorId
        self.connectedTo = {} # {Vertex-id : Vertex}


    def addNeighbor(self, vertex):
        self.connectedTo[vertex.id] = vertex


    def removeNeighbor(self, vertex_id):
        if vertex_id in self.connectedTo:
            del self.connectedTo[vertex_id]

    def __str__(self):
        return str(self.id)

    def isConnectedTo(self, vertex_id):
        return vertex_id in self.connectedTo
    
    def getId(self):
        return self.id
    
    def getAdjecentVertices(self) -> list:
        return [x for x in self.connectedTo.values()]
    
    def getColorId(self):
        return self.colorId
    
    def setColor(self, colorId):
        self.colorId = colorId


class Graph:
    def __init__(self):
        self.vertList = {} # {Vertex-id : Vertex}  

    def addVertex(self, vertex):
        self.vertList[vertex.id] = vertex

    def addEdge(self, vertex1_id, vertex2_id):
        if vertex1_id in self.vertList and vertex2_id in self.vertList:
            self.vertList[vertex1_id].addNeighbor(self.vertList[vertex2_id])
            self.vertList[vertex2_id].addNeighbor(self.vertList[vertex1_id])
        
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def resetColors(self):
        for vertex in self.vertList.values():
            vertex.setColor(None)

    def getVertices(self) -> list[Vertex]:
        return [x for x in self.vertList.values()]
    
    def removeVertex(self, vertex_id):
        if vertex_id in self.vertList:
            for vertex in self.vertList[vertex_id].getAdjecentVertices():
                vertex.removeNeighbor(vertex_id)
            del self.vertList[vertex_id]

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.vertList and vertex2 in self.vertList:
            self.vertList[vertex1.id].removeNeighbor(vertex2.id)
            self.vertList[vertex2.id].removeNeighbor(vertex1.id)

    def isAdjecent(self, vertex1_id, vertex2_id):
        if vertex1_id in self.vertList and vertex2_id in self.vertList:
            return self.vertList[vertex1_id].isConnectedTo(vertex2_id)
        else:
            return False
    
    def __len__(self):
        return len(self.vertList)