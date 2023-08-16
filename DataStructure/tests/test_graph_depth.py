from graph.graph_depth import Graph

def test_depth_first():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("D", "G")

    assert graph.depth_first("A") == ["A", "B", "D", "G", "E", "C", "F"]
    assert graph.depth_first("B") == ["B", "D", "G", "E"]
    assert graph.depth_first("C") == ["C", "F"]

    print("All test assertions passed.")

if __name__ == "__main__":
    test_depth_first()
