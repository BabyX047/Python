# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    # All possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    # Check if any winning combination is fulfilled
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_tie(board):
    return " " not in board

# Function to handle a player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move <= 8 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main function to run the game
def play_game():
    # Initial empty board
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Player makes a move
        player_move(board, current_player)
        print_board(board)
        
        # Check if the current player has won
        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        
        # Check if the game is a tie
        if check_tie(board):
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
