# Initialize variables
book_names = []  # Use a list to collect book names temporarily
book_count = 0  # Initialize a counter

# Loop to get 5 book names
while book_count < 5:
    name = input("Please enter a book name: ")  # Ask user for a book name
    book_names.append(name)  # Add the book name to the list
    book_count += 1  # Increment the counter

# Convert the list to a tuple
book_names_tuple = tuple(book_names)

# Display the names of the books
print("Books entered:")
for book in book_names_tuple:
    print(book)
