class Graph:
    """
    A class representing an undirected graph.

    Attributes:
        vertices (dict): A dictionary where the keys are vertices and the values are lists of neighboring vertices with associated weights.
    
    Methods:
        __init__(): Initializes an empty graph with no vertices or edges.
        add_vertex(value): Adds a vertex to the graph with the specified value if it doesn't already exist.
        add_edge(vertex1, vertex2, weight=None): Adds an undirected edge between vertex1 and vertex2 with an optional weight.
        get_vertices(): Returns a list of all vertices in the graph.
        get_neighbors(vertex): Returns a list of neighboring vertices for the given vertex.
        size(): Returns the number of vertices in the graph.
    """

    def __init__(self):
        """
        Initializes an empty graph with no vertices or edges.
        """
        self.vertices = {}
        self.graph = {}
    def add_vertex(self, value):
        """
        Adds a vertex to the graph with the specified value if it doesn't already exist.

        Args:
            value: The value associated with the new vertex.

        Returns:
            The value of the added vertex.
        """
        if value not in self.vertices:
            self.vertices[value] = []
        return value
    
    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Adds an undirected edge between vertex1 and vertex2 with an optional weight.

        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
            weight (optional): The weight of the edge.

        Note:
            If either vertex1 or vertex2 is not in the graph, the edge will not be added.
        """
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, weight))
            self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        """
        Returns a list of all vertices in the graph.

        Returns:
            A list of vertices.
        """
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        """
        Returns a list of neighboring vertices for the given vertex.

        Args:
            vertex: The vertex for which to retrieve neighbors.

        Returns:
            A list of neighboring vertices with associated weights.
        """
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []
    
    def size(self):
        """
        Returns the number of vertices in the graph.

        Returns:
            The number of vertices.
        """
        return len(self.vertices)
    
    def add_edge(self, city1, city2, cost):
        """
        Adds a directed edge between city1 and city2 with the specified cost.

        Args:
            city1: The source city.
            city2: The destination city.
            cost: The cost of the edge between the cities.
        """
        if city1 not in self.graph:
            self.graph[city1] = {}
        self.graph[city1][city2] = cost
    
    def get_cost(self, city1, city2):
        """
        Returns the cost of the edge between city1 and city2, if it exists.

        Args:
            city1: The source city.
            city2: The destination city.

        Returns:
            The cost of the edge if it exists, otherwise None.
        """
        if city1 in self.graph and city2 in self.graph[city1]:
            return self.graph[city1][city2]
        return None
    
# Example usage
graph = Graph()

v1 = graph.add_vertex("A")
v2 = graph.add_vertex("B")
v3 = graph.add_vertex("C")

graph.add_edge(v1, v2, 5)
graph.add_edge(v2, v3, 3)
graph.add_edge(v3, v1, 2)

# print("Vertices:", graph.get_vertices())
# print("Neighbors of v1:", graph.get_neighbors(v1))
# print("Number of vertices:", graph.size())
