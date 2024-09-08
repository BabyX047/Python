import random

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.\n")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
