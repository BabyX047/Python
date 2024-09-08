import random

# Function to get user choice
def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors or Exit: ").lower()
    while user_choice not in ["rock", "paper", "scissors", "exit"]:
        user_choice = input("Invalid choice. Enter rock, paper, or scissors or Exit: ").lower()
    return user_choice

# Function to get computer choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to play continuous score game mode
def play_continuous_score_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        if user_choice == "exit":
            print(f"Final Scores: You - {user_score}, Computer - {computer_score}\n")
            print("Bye, Bye!\n")
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.\n")
        
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie! Let's try again.\n")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: You - {user_score}, Computer - {computer_score}\n")

# Function to play best-of match mode
def play_best_of_game(best_of):
    user_score = 0
    computer_score = 0
    rounds_needed = (best_of // 2) + 1

    while user_score < rounds_needed and computer_score < rounds_needed:
        user_choice = get_user_choice()

        if user_choice == "exit":
            print(f"Final Scores: You - {user_score}, Computer - {computer_score}")
            print("Bye, Bye!")
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.\n")
        
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie! Let's try again.\n")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: You - {user_score}, Computer - {computer_score}\n")

    if user_score > computer_score:
        print("Congratulations, you won the series!")
    else:
        print("Computer won the series.")

# Function to select game mode
def game_mode_selection():
    while True:
        print("\nSelect Game Mode:")
        print("1. Continuous Score Mode (play until you type 'Exit').")
        print("2. Best of Match Mode (decide how many rounds to play).")
        mode_choice = input("Enter 1 or 2: ")

        if mode_choice == "1":
            print("\nYou selected Continuous Score Mode.")
            play_continuous_score_game()
            break
        elif mode_choice == "2":
            try:
                best_of = int(input("\nYou selected Best of Match Mode. How many rounds (odd number)?: "))
                if best_of % 2 == 0 or best_of <= 0:
                    print("Please enter a valid odd number greater than 0.")
                else:
                    play_best_of_game(best_of)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid choice, please select 1 or 2.")

# Main function to run the game
if __name__ == "__main__":
    game_mode_selection()
