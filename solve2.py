def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def hill_climbing(n):
    board = [-1] * n  

    for row in range(n):
        min_attacks = float('inf')
        best_col = -1


        for col in range(n):
            board[row] = col
            attacks = sum(1 for i in range(row) if not is_safe(board, i, board[i]))

            if attacks < min_attacks:
                min_attacks = attacks
                best_col = col

        board[row] = best_col

    return [[('Q' if j == board[i] else '.') for j in range(n)] for i in range(n)]

if __name__ == "__main__":
    
    board_size = 8

    
    solution = hill_climbing(board_size)

   
    print("Final Solution:")
    print_board(solution)
