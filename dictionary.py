person_info = {}

try:
    user_input = input("Enter your name, age, and favorite color (separated by commas): ")

    inputs = user_input.split(',')

    # Check if all three pieces of information were provided
    if len(inputs) != 3:
        raise ValueError("You must provide exactly three pieces of information: name, age, and favorite color.")

    # Strip whitespace from the inputs and assign them to the dictionary
    name, age, favorite_color = [item.strip() for item in inputs]
    person_info['Name'] = name
    person_info['Age'] = age
    person_info['Favorite Color'] = favorite_color

    # Print the dictionary
    print(person_info)

except ValueError as e:
    # Print an error message if the input was incorrect
    print(f"Error: {e}")





# Iteration two?