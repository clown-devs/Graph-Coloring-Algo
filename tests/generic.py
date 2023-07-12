import unittest
from src.models import *
from src.algo.greedy import *
from src.generator import *
from utils import *


class GenericColoringTest(unittest.TestCase):
    algorithm = None
    def test_empty_graph(self):
        self.assertEqual(self.algorithm(Graph()), 0)
    
    def test_random_graph(self):
        for i in range(1, 100):
            g = generate_graph(i)
            self.algorithm(g)
            self.assertTrue(is_corrected_colored(g))