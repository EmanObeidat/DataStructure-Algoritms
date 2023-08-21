## White board:
![wb](./Untitled%20(17).jpg)
## Approach and effiency:
traversing all graph nodes and return its Vertix ordered by depth First
## Solution:
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
## Big o:
Time and space complexity are O(n)