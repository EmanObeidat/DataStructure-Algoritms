# Approach and effiency :
```
The graph is implemented using an adjacency list representation. Each vertex is stored as a key in a dictionary, and its corresponding value is a list of tuples representing its neighbors and the weight of the edge connecting them. This approach allows for efficient storage and retrieval of vertex and edge information.
```
```
Efficiency:

Adding a Vertex (add_vertex): Adding a vertex involves inserting a key-value pair in a dictionary. The time complexity for this operation is O(1) on average, as dictionary insertion and retrieval are highly optimized.

Adding an Edge (add_edge): Adding an edge involves appending a tuple to the adjacency lists of two vertices. This operation takes O(1) time since it involves appending to a list.

Retrieving All Vertices (get_vertices): Retrieving all vertices involves returning the keys of the dictionary. Since the vertices are stored in a dictionary, this operation takes O(V) time, where V is the number of vertices in the graph.

Retrieving Neighbors (get_neighbors): Retrieving neighbors involves fetching the corresponding list of neighbors for a given vertex. This operation takes O(1) time on average since dictionary lookup is constant time.

Size (size): Getting the number of vertices simply involves returning the length of the dictionary, which takes O(1) time.
```
## [Code](./graph.py)

## [Test](../../DataStructure/tests/test_graph.py)