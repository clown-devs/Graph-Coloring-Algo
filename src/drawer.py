from pyvis.network import Network
from .models import *
from .color_generator import *
class Drawer():
    def __init__(self, Graph):
        self.net = Network(notebook=True)
        self.color_gen = ColorGenerator.get_instance()
        #TODO naive color generator logic
        colors = [
            '#0000FF', '#00FF00', '#FF0000', '0F0F0F', '#FFFF00', '#00FFFF', '#FF00FF', '#FFFFFF'
        ]

        for vertex in Graph.getVertices():
            self.net.add_node(vertex.id, color=self.color_gen.get_color(vertex.colorId))

            for adjecentVertex in vertex.getAdjecentVertices():
                self.net.add_node(adjecentVertex.id, color=self.color_gen.get_color(adjecentVertex.colorId))
                self.net.add_edge(vertex.id, adjecentVertex.id, weight=1)
    
    def draw(self, filename):
        self.net.toggle_physics(True)
        self.net.show(filename)
