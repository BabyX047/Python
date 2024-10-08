import random

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
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return all(space in ['X', 'O'] for space in board)

# Function to handle a player's move
def player_move(board, player_name, player_symbol):
    while True:
        try:
            move = int(input(f"{player_name} ({player_symbol}), enter your move (1-9): \n")) - 1
            if move >= 0 and move <= 8 and board[move] not in ['X', 'O']:
                board[move] = player_symbol
                break
            else:
                print("Invalid move. Please try again.\n")
        except ValueError:
            print("Please enter a number between 1 and 9.\n")

# Function for computer's move
def computer_move(board, computer_symbol):
    available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
    move = random.choice(available_moves)
    board[move] = computer_symbol

# Function to ask for replay
def replay():
    return input("Do you want to play again? (yes/no): \n").lower() == "yes"

# Main function to run the game
def play_game():
    print("Welcome to Tic-Tac-Toe by Lewis!")
    
    player1_wins = 0
    player2_wins = 0
    computer_wins = 0

    while True:
        # Choose game mode
        mode = input("Choose game mode: 'P2P' (Player to Player) or 'PvC' (Player vs Computer): \n").upper()
        if mode not in ['P2P', 'PVC']:
            print("Invalid mode. Please choose again.\n")
            continue
        
        # Initial board labeled 1 through 9
        board = [str(i+1) for i in range(9)]
        
        player1_name = input("Please enter Player 1 name: \n").upper()
        
        if mode == 'P2P':
            player2_name = input("Please enter Player 2 name: \n").upper()
        else:
            player2_name = "Computer"
        
        print(f"\nHello {player1_name} and {player2_name}\n")
        print_board(board)

        current_player = player1_name
        current_symbol = "X"
        
        while True:
            # Player or computer makes a move
            if current_player == "Computer":
                computer_move(board, current_symbol)
                print(f"\nComputer's move ({current_symbol}):\n")
            else:
                player_move(board, current_player, current_symbol)
            
            print_board(board)
            
            # Check if the current player has won
            if check_win(board, current_symbol):
                print(f"\nCongratulations! {current_player} wins!\n")
                if current_player == player1_name:
                    player1_wins += 1
                elif current_player == player2_name:
                    player2_wins += 1
                else:
                    computer_wins += 1
                break
            
            # Check if the game is a tie
            if check_tie(board):
                print("It's a tie!")
                break
            
            # Switch players
            if current_player == player1_name:
                current_player = player2_name
                current_symbol = "O"
            else:
                current_player = player1_name
                current_symbol = "X"
        
        # Display score
        if mode == 'P2P':
            print(f"\nScore: {player1_name}: {player1_wins} | {player2_name}: {player2_wins}\n")
        else:
            print(f"\nScore: {player1_name}: {player1_wins} | Computer: {computer_wins}\n")
        
        # Replay prompt
        if not replay():
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
