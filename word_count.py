# Initialize the words list
words = []

# Loop until the user has entered at least 5 words
while len(words) < 5:
    # Determine the correct ordinal for the prompt
    word_number = len(words) + 1
    if word_number == 1:
        prompt = "Enter the first word: "
    elif word_number == 2:
        prompt = "Enter the second word: "
    elif word_number == 3:
        prompt = "Enter the third word: "
    else:
        prompt = f"Enter the {word_number}th word: "

    # Get the word from the user
    word = input(prompt)
    words.append(word)  # Add the word to the list

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Use list comprehension to create a new list with words that have an even number of characters
even_length_words = [word for word in words if len(word) % 2 == 0]

# Print the lists
print("\nOdd words are: ", odd_length_words)
print("\nEven words are: ", even_length_words)
