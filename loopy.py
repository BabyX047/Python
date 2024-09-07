def generate_multiplication_table(number, max_range=10):
    for i in range(1, max_range + 1):
        print(f"{number} x {i} = {number * i}")

while True:
    # Get user input for the number
    try:
        number = int(input("Enter a number to generate its multiplication table: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Ask if user wants to customize the maximum range for the table
    customize_range = input("Do you want to customize the maximum range for the table? (Y/N): ").lower()
    if customize_range == 'y':
        max_range = int(input("Enter the maximum range: "))
        generate_multiplication_table(number, max_range)
    else:
        generate_multiplication_table(number)

    # Ask if user wants to generate another table
    repeat = input("Would you like to generate another table? (Y/N): ").lower()
    if repeat != 'y':
        print("Goodbye!")
        break






start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for number in range(start, end + 1):
    print(f"\nMultiplication Table for {number}:")
    generate_multiplication_table(number)
