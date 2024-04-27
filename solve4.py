import random

def objective_function(x):
    # Example objective function, replace it with your own function
    return -(x ** 2)  # Minimize the square of x

def hill_climbing(initial_solution, step_size, max_iterations):
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        new_solution = current_solution + random.uniform(-step_size, step_size)
        new_value = objective_function(new_solution)

        if new_value > current_value:
            current_solution = new_solution
            current_value = new_value

    return current_solution, current_value

# Example usage:
initial_solution = random.uniform(-10, 10)
step_size = 0.1
max_iterations = 100

optimal_solution, optimal_value = hill_climbing(initial_solution, step_size, max_iterations)

print("Optimal Solution:", optimal_solution)
print("Optimal Value:", optimal_value)
