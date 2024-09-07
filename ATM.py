def atm_simulation():
    # Set initial values
    pin = "1234"  # Default PIN for simplicity
    balance = 1000  # Initial balance
    
    # User authentication loop
    for attempt in range(3):  # Allow 3 attempts to enter PIN
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            break
        else:
            print(f"Incorrect PIN. You have {2 - attempt} attempts left.")
    else:
        print("Too many incorrect attempts. Exiting...")
        return  # Exit the program if PIN is wrong after 3 attempts

    print("\nWelcome to the ATM!\n")

    while True:
        # Display the menu options
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            # Check balance
            print(f"\nYour current balance is: ${balance}\n")
        
        elif choice == "2":
            # Deposit money
            deposit_amount = float(input("Enter the amount to deposit: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"\n${deposit_amount} has been deposited. Your new balance is: ${balance}\n")
            else:
                print("Invalid deposit amount. Please enter a positive number.\n")
        
        elif choice == "3":
            # Withdraw money
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if 0 < withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"\n${withdraw_amount} has been withdrawn. Your new balance is: ${balance}\n")
            elif withdraw_amount > balance:
                print("Insufficient funds. Try a smaller amount.\n")
            else:
                print("Invalid withdrawal amount. Please enter a positive number.\n")
        
        elif choice == "4":
            # Exit the program
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            # Invalid menu choice
            print("Invalid choice. Please select a valid option (1-4).\n")

# Start the ATM simulation
atm_simulation()
