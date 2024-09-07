# Function to get a set of integers from user input
def get_set_from_input(prompt):
    # Prompt the user to enter a list of integers separated by spaces
    input_string = input(prompt)
    # Convert the input string into a list of integers and then into a set
    input_set = set(map(int, input_string.split()))
    return input_set

# Get the first set from user input
set1 = get_set_from_input("Enter integers for the first set, separated by spaces: ")

# Get the second set from user input
set2 = get_set_from_input("Enter integers for the second set, separated by spaces: ")

# Create a new set that contains only the common elements
common_set = set1.intersection(set2)

# Display the result
print("The set of common elements is:", common_set)
