# def divisible_by_ten(num):
#     # Calculate the remainder when num is divided by 10
#     remainder = num % 10
    
#     # Check if the remainder is 0
#     return remainder == 0


# # Get user input

# testnum = []

# # Loop until the user has entered at least 3 Numbers
# while len(testnum) < 3:
#     num_number = len(testnum) + 1
#     if num_number == 1:
#         prompt = "Enter the first number: "
#     elif num_number == 2:
#         prompt = "Enter the second number: "
#     elif num_number == 3:
#         prompt = "Enter the third number: "
#     else:
#         prompt = f"Enter the {num_number}th number: "

#     # Get the numbers from the user
#     number = int(input(prompt))
#     testnum.append(number)  # Add the numbers to the list




# # Check if each number is divisible by 10
# for num in testnum:
#     if divisible_by_ten(num):
#         print(str(num) + " is divisible by 10")
#     else:
#         print(str(num) + " is not divisible by 10")


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
