class Graph:
    """
    A class representing an undirected graph and providing methods for graph operations.
    
    Attributes:
        graph (dict): A dictionary representing the graph structure where each node maps to its neighbors.
        
    Methods:
        __init__(): Initializes an empty graph.
        
        add_edge(node, neighbor): Adds an edge between the given node and neighbor in the graph.
        
        depth_first(node): Performs a depth-first traversal starting from the given node.
        
    """
    
    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}

    def add_edge(self, node, neighbor):
        """
        Adds an edge between the given node and neighbor in the graph.
        
        Args:
            node: The starting node of the edge.
            neighbor: The neighbor node connected to the starting node.
        """
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def depth_first(self, node):
        """
        Performs a depth-first traversal starting from the given node.
        
        Args:
            node: The starting node for the depth-first traversal.
        
        Returns:
            list: A list containing the nodes visited during the depth-first traversal.
        """
        visited = set()
        result = []

        def dfs(current_node):
            visited.add(current_node)
            result.append(current_node)
            
            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        dfs(neighbor)

        dfs(node)
        return result

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("D", "G")

    traversal_result_A = graph.depth_first("A")
    traversal_result_B = graph.depth_first("B")
    traversal_result_C = graph.depth_first("C")

    print("Depth-first traversal starting from node 'A':", traversal_result_A)
    print("Depth-first traversal starting from node 'B':", traversal_result_B)
    print("Depth-first traversal starting from node 'C':", traversal_result_C)
