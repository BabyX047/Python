import random

print("Welcome to my guessing game.\n")
print("I am thinking of a number.\n")

difficulty = input("Choose a difficulty level: Easy, Medium, or Hard: ").lower()

if difficulty == 'easy':
    number = random.randint(1, 20)
    max_attempts = 10
elif difficulty == 'medium':
    number = random.randint(1, 50)
    max_attempts = 7
else:
    number = random.randint(1, 100)
    max_attempts = 5

attempts = 0

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    attempts += 1
    print(f"You have {max_attempts - attempts} attempts remaining.")

    if attempts == 3:
        if number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")

    if attempts == max_attempts:
        print(f"Sorry, you ran out of attempts. The correct number was {number}.")

play_again = input("Do you want to play again? Y/N: ").lower()
if play_again == 'y':
    # Optionally reset everything and loop the game
    pass
else:
    print("Thanks for playing!")
