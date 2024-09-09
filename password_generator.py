import random
import string

# Function to generate password
def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Start with all lowercase letters
    character_pool = list(string.ascii_lowercase)
    
    # Add uppercase letters if selected
    if use_uppercase:
        character_pool += list(string.ascii_uppercase)
    
    # Add digits if selected
    if use_digits:
        character_pool += list(string.digits)
    
    # Add special characters if selected
    if use_special_chars:
        character_pool += list(string.punctuation)
    
    # Generate a random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Function to get user input
def get_password_criteria():
    # Get the length of the password
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask if the user wants to include uppercase letters, digits, and special characters
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, use_uppercase, use_digits, use_special_chars

# Main function
def main():
    print("Welcome to the Password Generator!")
    
    # Get the user's password criteria
    length, use_uppercase, use_digits, use_special_chars = get_password_criteria()
    
    # Generate the password based on the criteria
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
