class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def depth_first(self, node):
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
