import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.models import *
from src.algo.greedy import *
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


del GenericColoringTest

if __name__ == '__main__':
    unittest.main()