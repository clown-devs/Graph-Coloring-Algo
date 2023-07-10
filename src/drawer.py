from pyvis.network import Network
from .models import *

class Drawer():
    def __init__(self, Graph):
        self.net = Network(notebook=True)
        
        #TODO naive color generator logic
        colors = [
            '#0000FF', '#00FF00', '#FF0000', '0F0F0F', '#FFFF00', '#00FFFF', '#FF00FF', '#FFFFFF'
        ]

        for vertex in Graph.getVertices():
            self.net.add_node(vertex.id, color=colors[vertex.getColor()])
            for adjecentVertex in vertex.connectedTo.values():
                self.net.add_node(adjecentVertex.id, color=colors[adjecentVertex.colorId])
                self.net.add_edge(vertex.id, adjecentVertex.id, weight=1)
    
    def draw(self, filename):
        self.net.toggle_physics(True)
        self.net.show(filename)
