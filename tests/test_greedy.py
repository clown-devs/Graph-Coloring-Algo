import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.models import *
from src.algo.greedy import *
from src.generator import *
from utils import *

class GreedyBasicTests(unittest.TestCase):
    def setUp(self):  
        self.g = generate_graph(50)

    def tearDown(self):
        self.g = None

    def test_greedy_coloring(self):
        greedy_coloring(self.g)
        self.assertTrue(is_corrected_colored(self.g))

    def test_sorting_greedy_coloring(self):
        sorting_greedy_coloring(self.g)
        self.assertTrue(is_corrected_colored(self.g))


if __name__ == '__main__':
    unittest.main()