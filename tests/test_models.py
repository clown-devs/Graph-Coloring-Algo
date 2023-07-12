import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.models import *

class VertexTests(unittest.TestCase):
    def setUp(self):  
        self.vertex = Vertex(1) 
    
    def tearDown(self):
        self.vertex = None
    
    def test_add_adjecent_vertex(self):
        vertex2 = Vertex(2)
        self.vertex.addNeighbor(vertex2)
        self.assertIn(vertex2, self.vertex.getAdjecentVertices())

    def test_remove_adjecent_vertex(self):
        vertex2 = Vertex(2)
        self.vertex.addNeighbor(vertex2)
        self.vertex.removeNeighbor(2)
        self.assertNotIn(vertex2, self.vertex.getAdjecentVertices())

    def test_check_connection_one(self):
        vertex2 = Vertex(2)
        self.vertex.addNeighbor(vertex2)
        self.assertTrue(self.vertex.isConnectedTo(2))

    def test_check_connection_many(self):
        vertex_list = [Vertex(x) for x in range(2,11)]
        
        for vertex_id in range(2, len(vertex_list) // 2):
            self.vertex.addNeighbor(vertex_list[vertex_id - 2])
    
        for vertex_id in range(2, len(vertex_list) // 2):
            self.assertTrue(self.vertex.isConnectedTo(vertex_id))
        
        for vertex_id in range(len(vertex_list) // 2, len(vertex_list)):
            self.assertFalse(self.vertex.isConnectedTo(vertex_id))

    def test_get_id(self):
        self.assertEqual(self.vertex.getId(), 1)
    
    def test_get_adjecent_vertices(self):
        vertex_list = [Vertex(x) for x in range(2,10)]

        for vertex in vertex_list:
            self.vertex.addNeighbor(vertex)

        self.assertEqual(self.vertex.getAdjecentVertices(), vertex_list)

    def test_get_color(self):
        self.assertEqual(self.vertex.getColorId(), None)

    def test_set_color(self):
        self.vertex.setColor(1)
        self.assertEqual(self.vertex.getColorId(), 1)
    
        

class GraphTests(unittest.TestCase): 
    def setUp(self):  
        self.graph = Graph() 
    
    def tearDown(self):
        self.graph = None
    
    def test_add_one_vertex(self):
        vertex = Vertex(1)
        self.graph.addVertex(vertex)
        
        self.assertIn(vertex, self.graph.getVertices())

    def test_add_many_vertices(self):
        vertex_list = [Vertex(x) for x in range(1,10)]
        for vertex in vertex_list:
            self.graph.addVertex(vertex)
        
        self.assertEqual(self.graph.getVertices(), vertex_list)

    def test_get_vertices(self):
        vertex_list = [Vertex(x) for x in range(2,10)]
        for vertex in vertex_list:
            self.graph.addVertex(vertex)
        
        self.assertEqual(self.graph.getVertices(), vertex_list)

    def test_get_vertex(self):
        vertex = Vertex(1)
        self.graph.addVertex(vertex)
        
        self.assertEqual(self.graph.getVertex(1), vertex)

    def test_remove_one_vertex(self):
        vertex = Vertex(1)
        self.graph.addVertex(Vertex(1))
    
        self.graph.removeVertex(1)
        
        self.assertNotIn(vertex, self.graph.getVertices())

    def test_remove_many_vertices(self):
        vertex_list = [Vertex(x) for x in range(2,10)]
        for vertex in vertex_list:
            self.graph.addVertex(vertex)
        
        for vertex in vertex_list:
            self.graph.removeVertex(vertex.getId())
        
        self.assertEqual(self.graph.getVertices(), [])

    def test_add_one_edge(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        self.graph.addVertex(vertex1)
        self.graph.addVertex(vertex2)
        self.graph.addEdge(vertex1.getId(), vertex2.getId())
        
        self.assertTrue(self.graph.isAdjecent(vertex1.getId(), vertex2.getId()))

    def test_add_many_edges(self):
        vertex_list = [Vertex(x) for x in range(2,10)]
        for vertex in vertex_list:
            self.graph.addVertex(vertex)
        
        for vertex_id in range(2, len(vertex_list) // 2):
            self.graph.addEdge(1, vertex_id)
        
        for vertex_id in range(2, len(vertex_list) // 2 - 2):
            self.assertTrue(self.graph.isAdjecent(1, vertex_id))
        
        for vertex_id in range(len(vertex_list) // 2, len(vertex_list)):
            self.assertFalse(self.graph.isAdjecent(1, vertex_id))


    def test_remove_edge(self):
        vertex1 = Vertex(1)
        vertex2 = Vertex(2)
        self.graph.addVertex(vertex1)
        self.graph.addVertex(vertex2)
        self.graph.addEdge(vertex1, vertex2)
        
        self.graph.removeEdge(vertex1, vertex2)
        
        self.assertNotIn(vertex2, vertex1.getAdjecentVertices())
        self.assertNotIn(vertex1, vertex2.getAdjecentVertices())



if __name__ == '__main__':
    unittest.main()