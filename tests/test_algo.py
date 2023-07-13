import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.models import *
from src.algo.greedy import *
from src.algo.RLF import *
from src.generator import *
from src.algo.contraction import *
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


class ContractionTest(unittest.TestCase):
    def test_K3(self):
        g = Graph()
        g.addVertex(Vertex(1))
        g.addVertex(Vertex(2))
        g.addVertex(Vertex(3))
        
        g.addEdge(1, 2)
        g.addEdge(1, 3)
        g.addEdge(2, 1)
        g.addEdge(2, 3)
        g.addEdge(3, 1)
        g.addEdge(3, 2)
        colors = 3
        K3_polynom = lambda t: t * (t - 1) * (t - 2)
        self.assertEqual(contraction(g, colors)[0], K3_polynom(colors))
        self.assertEqual(contraction(g, colors)[1], 3)

    def test_Pn(self):
        for i in range(1, 12):
            g = Graph()
            for j in range(i):
                g.addVertex(Vertex(j + 1))
            vertices = g.getVertices()
            for k in range(len(vertices) - 1):
                g.addEdge(vertices[k].id, vertices[k + 1].id)
            
            Pn_polynom = lambda t, n: t * (t - 1) ** (n - 1)
            for c in range(10):
                self.assertEqual(contraction(g, colors=c)[0], Pn_polynom(c, len(g)))

    def test_Cn(self):
        for i in range(1, 12):
            g = Graph()
            for j in range(i):
                g.addVertex(Vertex(j + 1))
            vertices = g.getVertices()
            for k in range(len(vertices) - 1):
                g.addEdge(vertices[k].id, vertices[k + 1].id)
            g.addEdge(vertices[-1].id, vertices[0].id)
            
            Cn_polynom = lambda t, n: (t - 1)**n + ( (-1)**n ) * (t - 1) 
            for c in range(10):
                self.assertEqual(contraction(g, colors=c)[0], Cn_polynom(c, len(g)))

    def test_Petersen_graph(self):
        g = Graph()
        for i in range(1, 11):
            g.addVertex(Vertex(i))
        
        # outer radius
        g.addEdge(1, 2)
        g.addEdge(1, 5)
        g.addEdge(2, 1)
        g.addEdge(2, 3)
        g.addEdge(3, 2)
        g.addEdge(3, 4)
        g.addEdge(4, 3)
        g.addEdge(4, 5)
        g.addEdge(5, 4)
        g.addEdge(5, 1)

        # star bounds
        g.addEdge(1, 6)
        g.addEdge(2, 7)
        g.addEdge(3, 8)
        g.addEdge(4, 9)
        g.addEdge(5, 10)

        #star iner edges
        g.addEdge(6, 8)
        g.addEdge(6, 9)
        g.addEdge(7, 9)
        g.addEdge(7, 10)
        g.addEdge(8, 6)
        g.addEdge(8, 10)
        g.addEdge(9, 6)
        g.addEdge(9, 7)
        g.addEdge(10, 7)
        g.addEdge(10, 8)

        Petersen_polynom = lambda t: t * (t - 1) * (t - 2) * (t**7 - 12 * t**6 + 67 * t**5 - 230 * t**4 + 529 * t**3 - 814 * t**2 + 775 * t - 352)
        for t in range(10):
            self.assertEqual(contraction(g, colors=t)[0], Petersen_polynom(t))


del GenericColoringTest


if __name__ == '__main__':
    unittest.main()