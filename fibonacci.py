#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    user_input = input("How many terms do you want in the Fibonacci sequence? ")

    if not user_input.isdigit():  # input must be digits
        print("Please enter a positive integer.")
        continue

    n_terms = int(user_input)
    if n_terms <= 0:
        print("Please enter a positive integer.")
    else:
        break

# Generate and print Fibonacci sequence
a, b = 0, 1
for i in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
print()


