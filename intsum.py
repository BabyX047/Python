intinput = input("Please enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
int_list = [int(x) for x in intinput.split()]

# Process the list (example: printing each integer)
for i in int_list:
    print(f"Integer: {i}")

# Compute the sum of the list
total_sum = sum(int_list)

# Print the entire list of integers and the sum
print(f"Input list is: {int_list}")
print(f"Sum is: {total_sum}")
