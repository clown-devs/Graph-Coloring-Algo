import random

class ColorGenerator:
    _instance = None
    
    @staticmethod
    def get_instance():
        if not ColorGenerator._instance:
            ColorGenerator._instance = ColorGenerator()
        return ColorGenerator._instance
    
    def __init__(self):
        self.colors = list()
    
    def generate_color(self):
        while True:
            color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
            if color not in self.colors:
                self.colors.append(color)
                return color
            
    def get_color(self, color_id):
        while color_id >= len(self.colors):
            self.generate_color()
        return self.colors[color_id]

    def __len__(self):
        return len(self.colors)