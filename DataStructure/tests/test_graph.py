import pytest
from graph.graph import Graph


def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    assert graph.get_vertices() == ["A", "B"]




# Run the tests
if __name__ == "__main__":
    test_add_vertex()
    test_add_edge()
    test_get_cost()
    print("All tests passed!")
