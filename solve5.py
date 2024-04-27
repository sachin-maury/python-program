import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, graph, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.state)

        for neighbor, cost in graph.get(current_node.state, {}).items():
            if neighbor not in closed_set:
                new_cost = current_node.cost + cost
                new_node = Node(neighbor, current_node, new_cost, heuristic(neighbor, goal))

                if new_node not in open_set:
                    heapq.heappush(open_set, new_node)

    return None  # No path found

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
goal_node = 'D'

def heuristic(node, goal):
    return 0  # No heuristic (Dijkstra's algorithm)

result = astar(start_node, goal_node, graph, heuristic)

if result:
    print("Optimal Path:", result)
else:
    print("No path found.")
