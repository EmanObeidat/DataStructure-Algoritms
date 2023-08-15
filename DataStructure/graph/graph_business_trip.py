from graph.graph import Graph

def business_trip(graph, cities):
    """
    Calculates the total cost of a business trip through the specified cities using the provided graph.

    Args:
        graph (Graph): The graph representing city connections and costs.
        cities (list): A list of cities representing the trip route.

    Returns:
        The total cost of the trip, or None if the trip is not possible.
    """
    if len(cities) < 2:
        print("Trip is not possible due to insufficient cities.")
        return None
    
    total_cost = 0
    for i in range(len(cities) - 1):
        cost = graph.get_cost(cities[i], cities[i+1])
        if cost is None:
            print(f"No direct flight available from {cities[i]} to {cities[i+1]}. Trip is not possible.")
            return None
        total_cost += cost
    
    print(f"Total cost of the trip: {total_cost}")
    return total_cost

# Test graph and cities
test_graph = Graph()
test_graph.add_edge('A', 'B', 100)
test_graph.add_edge('B', 'C', 150)
test_graph.add_edge('C', 'D', 200)
test_graph.add_edge('D', 'E', 120)

cities = ['A', 'B', 'C']
business_trip(test_graph, cities)
