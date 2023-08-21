def adjacency_matrix_to_list(nodes, matrix):
    adjacency_list = {}
    
    for i in range(len(nodes)):
        adjacency_list[nodes[i]] = [] 
        
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjacency_list[nodes[i]].append(nodes[j])  
    
    return adjacency_list
    
nodes = ['A', 'B', 'C', 'D']
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]

adjacency_list = adjacency_matrix_to_list(nodes, matrix)
print(adjacency_list)
