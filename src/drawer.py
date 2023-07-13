from pyvis.network import Network
from .models import *
from .color_generator import *

class Drawer():
    def __init__(self, Graph, drawId=False):
        self.net = Network(notebook=True)
        self.color_gen = ColorGenerator.get_instance()
        
        for vertex in Graph.getVertices():
            if drawId:
                self.net.add_node(vertex.id, label=str(vertex), color=self.color_gen.get_color(vertex.colorId))
            else:
                self.net.add_node(vertex.id, color=self.color_gen.get_color(vertex.colorId))

            for adjecentVertex in vertex.getAdjecentVertices():
                if drawId:
                    self.net.add_node(adjecentVertex.id, label=str(adjecentVertex), color=self.color_gen.get_color(adjecentVertex.colorId))
                else:
                    self.net.add_node(adjecentVertex.id, color=self.color_gen.get_color(adjecentVertex.colorId))
                self.net.add_edge(vertex.id, adjecentVertex.id, weight=1)
    
    def draw(self, filename):
        self.net.toggle_physics(True)
        self.net.show(filename)
