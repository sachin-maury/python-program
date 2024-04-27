from queue import Queue

def tsp_bfs(graph, start):
    n = len(graph)
    visited = set()
    queue = Queue()
    queue.put((start, [start], 0))

    while not queue.empty():
        current, path, cost = queue.get()

        if len(path) == n:
            # If all cities are visited, go back to the starting city
            path.append(start)
            return path, cost + graph[current][start]

        for neighbor in range(n):
            if neighbor not in path:
                new_path = path.copy()
                new_path.append(neighbor)
                new_cost = cost + graph[current][neighbor]
                queue.put((neighbor, new_path, new_cost))

    return None, float('inf')

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0
path, cost = tsp_bfs(graph, start_city)

if path is not None:
    print("Optimal TSP Path:", path)
    print("Total Cost:", cost)
else:
    print("No solution found.")
