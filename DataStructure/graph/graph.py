class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []
        return value
    
    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, weight))
            self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []
    
    def size(self):
        return len(self.vertices)



graph = Graph()

v1 = graph.add_vertex("A")
v2 = graph.add_vertex("B")
v3 = graph.add_vertex("C")

graph.add_edge(v1, v2, 5)
graph.add_edge(v2, v3, 3)
graph.add_edge(v3, v1, 2)

print("Vertices:", graph.get_vertices())
print("Neighbors of v1:", graph.get_neighbors(v1))
print("Number of vertices:", graph.size())
