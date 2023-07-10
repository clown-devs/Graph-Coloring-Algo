from pyvis.network import Network
from .models import *

class Drawer():
    def __init__(self, Graph):
        self.net = Network(notebook=True)
        
        for vertex in Graph.vertList.values():
            self.net.add_node(vertex.id, color=vertex.getColor())
            for adjecentVertex in vertex.connectedTo.values():
                self.net.add_node(adjecentVertex.id, color=adjecentVertex.color)
                self.net.add_edge(vertex.id, adjecentVertex.id, weight=1)
    
    def draw(self, filename):
        self.net.toggle_physics(True)
        self.net.show(filename)
