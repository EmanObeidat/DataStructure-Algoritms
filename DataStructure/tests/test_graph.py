import pytest
from graph.graph import Graph

def test_graph():
    graph = Graph()

    v1 = graph.add_vertex("A")
    assert v1 in graph.get_vertices()

    v2 = graph.add_vertex("B")
    graph.add_edge(v1, v2, 3)
    neighbors_v1 = graph.get_neighbors(v1)
    assert (v2, 3) in neighbors_v1
    neighbors_v2 = graph.get_neighbors(v2)
    assert (v1, 3) in neighbors_v2

    all_vertices = graph.get_vertices()
    assert len(all_vertices) == 2
    assert v1 in all_vertices
    assert v2 in all_vertices

    neighbors_v1 = graph.get_neighbors(v1)
    assert len(neighbors_v1) == 1
    assert neighbors_v1[0][0] == v2

    assert neighbors_v1[0][1] == 3

    assert graph.size() == 2

    v3 = graph.add_vertex("C")
    graph.add_edge(v2, v3, 2)
    assert graph.size() == 3
    neighbors_v3 = graph.get_neighbors(v3)
    assert len(neighbors_v3) == 1
    assert neighbors_v3[0][0] == v2
    assert neighbors_v3[0][1] == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_graph()
