
######## GAME ######

def divisible_by_ten(num):
    # Calculate the remainder when num is divided by 10
    remainder = num % 10
    
    # Check if the remainder is 0
    return remainder == 0

# Game loop
while True:
    # Get user input
    testnum = int(input("Enter a number: "))

    # Check if the number is divisible by 10
    if divisible_by_ten(testnum):
        print(str(testnum) + " is divisible by 10. You win!")
        break  # Exit the loop
    else:
        print(str(testnum) + " is not divisible by 10. Try again.")
