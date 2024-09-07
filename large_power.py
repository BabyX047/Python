def large_power(base, exponent):
    # Calculate the result of base raised to the power of exponent
    result = base ** exponent
    
    # Check and return a tuple with the result and its conditions
    is_greater_than_5000 = result > 5000
    is_even = result % 2 == 0
    return result, is_greater_than_5000, is_even

# Receive input from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))

# Call the function with the user-provided inputs and store the result
result, is_greater_than_5000, is_even = large_power(base, exponent)

# Print the appropriate message based on the conditions
if is_greater_than_5000 and is_even:
    print(f"The result is {result}, which is greater than 5000 and is an even number.")
elif is_greater_than_5000 and not is_even:
    print(f"The result is {result}, which is greater than 5000 and is an odd number.")
elif not is_greater_than_5000 and not is_even:
    print(f"The result is {result}, which is not greater than 5000 and is an odd number.")
else:
    print(f"The result is {result}, which is not greater than 5000 and is an even number.")
