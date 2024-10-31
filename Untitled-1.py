# Tic-Tac-Toe Game in Python with Input Validation

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def check_draw(board):
    return all([spot != " " for row in board for spot in row])


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
            
            # Check for valid input range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
            
            # Check if the spot is already taken
            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue

            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the game
tic_tac_toe()
