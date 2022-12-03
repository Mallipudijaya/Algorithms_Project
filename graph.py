import vertex as vtx
import random
class edge:
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w

     
class Graph:
    def __init__(self,num):
        self.vertices = [[]]*num
        self.adjacency_matrix=[([0]*num) for i in range(num)]
    
    def add_vertex(self, vertex):
        if isinstance(vertex, vtx.Vertex):
            self.vertices[vertex.name] = vertex.neighbors

            
    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, vtx.Vertex):
                self.vertices[vertex.name] = vertex.neighbors
            
    def add_edge(self, vertex_from, vertex_to, i, j):
        
        self.adjacency_matrix[i][j] = self.adjacency_matrix[j][i] = random.randint(1,20)
        if isinstance(vertex_from, vtx.Vertex) and isinstance(vertex_to, vtx.Vertex):
            vertex_from.add_neighbor(vertex_to)
            if isinstance(vertex_from, vtx.Vertex) and isinstance(vertex_to, vtx.Vertex):
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors      
    
    def adjacencyList(self):
        if len(self.vertices) >= 1: 
                return [ (self.vertices[key]) for key in range(len(self.vertices))]  
        else:
            return dict()   
    def adjacencyList_mst(self):
        
        if len(self.vertices) >= 1: 
                return [ (self.vertices[i]) for i in range(len(self.vertices))]  
                
        else:
            return [[]]  

    def add_edge_mst(self, vertex_from, vertex_to):
        if isinstance(vertex_from, vtx.Vertex) and isinstance(vertex_to, vtx.Vertex):
            vertex_from.add_neighbor(vertex_to)
            #if isinstance(vertex_from, vtx.Vertex) and isinstance(vertex_to, vtx.Vertex):
            self.vertices[vertex_from.name] = vertex_from.neighbors
            self.vertices[vertex_to.name] = vertex_to.neighbors