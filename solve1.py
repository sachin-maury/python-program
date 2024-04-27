from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def print_puzzle(state):
    for row in state:
        print(row)

def find_blank(state):
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def apply_move(state, move):
    i, j = find_blank(state)
    new_i, new_j = i + move[0], j + move[1]

    if is_valid_move(new_i, new_j):
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
        return new_state
    else:
        return None

def is_goal_state(state):
    return state == goal_state

def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if is_goal_state(current_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        for move in moves:
            new_state = apply_move(current_state, move)
            if new_state and tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [move]))

    return None

if __name__ == "__main__":
    initial_state = [[1, 2, 3],
                     [4, 0, 6],
                     [7, 5, 8]]

    print("Initial State:")
    print_puzzle(initial_state)

    result = bfs(initial_state)

    if result:
        print("\nSolution Path:")
        for move in result:
            print(move)
    else:
        print("\nNo solution found.")
