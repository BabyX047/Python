import random

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors or Exit: ").lower()
    while user_choice not in ["rock", "paper", "scissors", "exit"]:
        user_choice = input("Invalid choice. Enter rock, paper, or scissors or Exit: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
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


if __name__ == "__main__":
    play_game()
