def calculate_total_distance(order, distance_matrix):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distance_matrix[order[i]][order[i + 1]]
    total_distance += distance_matrix[order[-1]][order[0]]  
    return total_distance

def simulated_annealing_tsp(distance_matrix, temperature=1000, cooling_rate=0.95, iterations=1000):
    num_cities = len(distance_matrix)
    current_order = list(range(num_cities))
    current_distance = calculate_total_distance(current_order, distance_matrix)

    best_order = current_order.copy()
    best_distance = current_distance
    
    for iteration in range(iterations):
        new_order = current_order.copy()
        i, j = sorted(random.sample(range(num_cities), 2))
        new_order[i:j+1] = reversed(new_order[i:j+1])

        new_distance = calculate_total_distance(new_order, distance_matrix)

        if new_distance < current_distance or random.uniform(0, 1) < math.exp((current_distance - new_distance) / temperature):
            current_order = new_order
            current_distance = new_distance

        if new_distance < best_distance:
            best_order = new_order
            best_distance = new_distance

        temperature *= cooling_rate

    return best_order, best_distance


distance_matrix = np.array([[0, 2, 9, 10],
                            [1, 0, 6, 4],
                            [15, 7, 0, 8],
                            [6, 3, 12, 0]])


best_order, best_distance = simulated_annealing_tsp(distance_matrix)
print("Best Order:", best_order)
print("Best Distance:", best_distance)
