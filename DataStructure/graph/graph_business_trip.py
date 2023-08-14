class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, city1, city2, cost):
        if city1 not in self.graph:
            self.graph[city1] = {}
        self.graph[city1][city2] = cost
        
    def get_cost(self, city1, city2):
        if city1 in self.graph and city2 in self.graph[city1]:
            return self.graph[city1][city2]
        return None


def business_trip(graph, cities):
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


test_graph = Graph()
test_graph.add_edge('A', 'B', 100)
test_graph.add_edge('B', 'C', 150)
test_graph.add_edge('C', 'D', 200)
test_graph.add_edge('D', 'E', 120)

cities = ['A', 'B', 'C']
business_trip(test_graph, cities)