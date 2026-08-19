# Question:
# Write a Python program to print the Fibonacci series
# up to n terms using iteration.


num = int(input("Enter a number: "))


def fibonacci(n):

    # First two Fibonacci numbers
    a, b = 0, 1

    # Repeat n times
    for i in range(n):

        # Print current Fibonacci number
        print(a, end=" ")

        # Calculate next number
        c = a + b

        # Move a and b forward
        a = b
        b = c


# Function call
fibonacci(num)


# Execution Example:
#
# Input:
# 5
#
# Initially:
# a = 0, b = 1
#
# i = 0 → print 0
# c = 0 + 1 = 1
# a = 1, b = 1
#
# i = 1 → print 1
# c = 1 + 1 = 2
# a = 1, b = 2
#
# i = 2 → print 1
# c = 1 + 2 = 3
# a = 2, b = 3
#
# i = 3 → print 2
# c = 2 + 3 = 5
# a = 3, b = 5
#
# i = 4 → print 3
#
# Output:
# 0 1 1 2 3


# Time Complexity: O(n)
# Space Complexity: O(1)