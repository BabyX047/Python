def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

# Ask the user to input the value of n
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fib_sequence = generate_fibonacci(n)

# Print the generated Fibonacci sequence
print("Fibonacci sequence up to term", n, "is", fib_sequence)
