import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.models import *
from src.algo.greedy import *
from src.algo.RLF import *
from src.generator import *
from utils import *

# Abstract Class
class GenericColoringTest(unittest.TestCase):
    def algorithm(self, g: Graph):
        pass

    def test_empty_graph(self):

        self.assertEqual(self.algorithm(Graph()), 0)
    
    def test_random_graph(self):
        for i in range(1, 100):
            g = generate_graph(i)
            self.algorithm(g)
            self.assertTrue(is_corrected_colored(g))


class GreedyColoringTest(GenericColoringTest):
    def algorithm(self, g: Graph):
        return greedy_coloring(g)
    

class GreedySortingColoringTest(GenericColoringTest):
    def algorithm(self, g: Graph):
        return sorting_greedy_coloring(g)


class RLFTest(GenericColoringTest):
    def algorithm(self, g: Graph):
        return RLF(g)
    
    def test_max_neighbours(self):
        g = Graph()

        self.assertEqual(get_max_neighbours_vertex(g), None)

        g.addVertex(Vertex(1))
        g.addVertex(Vertex(2))
        g.addVertex(Vertex(3))
        g.addVertex(Vertex(4))
        g.addVertex(Vertex(5))
        g.addEdge(1,2)

        self.assertEqual(get_max_neighbours_vertex(g), g.getVertex(1))
        
        g.addEdge(2,3)
        self.assertEqual(get_max_neighbours_vertex(g), g.getVertex(2))
        g.addEdge(3,4)
        g.addEdge(3,5)
        self.assertEqual(get_max_neighbours_vertex(g), g.getVertex(3))

        g.removeVertex(3)
        self.assertEqual(get_max_neighbours_vertex(g), g.getVertex(1))

    def test_not_adjecent_to_all(self):
        g = Graph()
        g.addVertex(Vertex(1))
        g.addVertex(Vertex(2))
        g.addVertex(Vertex(3))
        g.addVertex(Vertex(4))
        g.addVertex(Vertex(5))
        g.addEdge(1,2)
        g.addEdge(2,3)
        g.addEdge(3,4)
        g.addEdge(4,5)
        g.addEdge(5,1)
        g.addEdge(5,2)
        g.addEdge(5,3)
        g.addEdge(5,4)

        self.assertTrue(not_adjecent_to_all(g.getVertex(1), []))
        self.assertFalse(not_adjecent_to_all(g.getVertex(1), [g.getVertex(1)]))

        self.assertFalse(not_adjecent_to_all(g.getVertex(1), [g.getVertex(2)]))
        self.assertFalse(not_adjecent_to_all(g.getVertex(1), [g.getVertex(2), g.getVertex(3)]))
        self.assertTrue(not_adjecent_to_all(g.getVertex(1), [g.getVertex(3), g.getVertex(4)]))
        self.assertFalse(not_adjecent_to_all(g.getVertex(1), [g.getVertex(2), g.getVertex(3), g.getVertex(4)]))
        self.assertFalse(not_adjecent_to_all(g.getVertex(1), [g.getVertex(2), g.getVertex(3), g.getVertex(4), g.getVertex(5)]))
        self.assertFalse(not_adjecent_to_all(g.getVertex(5), [g.getVertex(3), g.getVertex(4), g.getVertex(5)]))
        self.assertTrue(not_adjecent_to_all(g.getVertex(2), [g.getVertex(4)]))

del GenericColoringTest

if __name__ == '__main__':
    unittest.main()