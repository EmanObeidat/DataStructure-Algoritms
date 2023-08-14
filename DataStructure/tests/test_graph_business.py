import pytest
from graph.graph_business_trip import Graph, business_trip

def test_valid_trip():
    test_graph = Graph()
    test_graph.add_edge('A', 'B', 100)
    test_graph.add_edge('B', 'C', 150)
    test_graph.add_edge('C', 'D', 200)
    test_graph.add_edge('D', 'E', 120)
    
    assert business_trip(test_graph, ['A', 'B', 'C']) == 250

def test_invalid_trip():
    test_graph = Graph()
    test_graph.add_edge('A', 'B', 100)
    test_graph.add_edge('B', 'C', 150)
    test_graph.add_edge('C', 'D', 200)
    test_graph.add_edge('D', 'E', 120)
    
    assert business_trip(test_graph, ['A', 'C', 'E']) is None
    assert business_trip(test_graph, ['A']) is None
    assert business_trip(test_graph, []) is None

if __name__ == "__main__":
    pytest.main()
