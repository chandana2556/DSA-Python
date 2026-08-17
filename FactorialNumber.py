# Question:
# Write a recursive Python program to find the factorial of a given number.

# Take input from the user
num = int(input("Enter a number: "))


# Recursive function to find factorial
def factorial(n):

    # Base Case:
    # When n becomes 0, stop the recursion
    if n == 0:
        return 1

    # Recursive Case:
    # Multiply n with factorial of n-1
    return n * factorial(n - 1)


# Call the function and print the result
print("Factorial =", factorial(num))


# Execution Example:
#
# Input:
# 5
#
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1 * factorial(0)
#
# factorial(0) = 1
#
# Therefore:
# 5 * 4 * 3 * 2 * 1 * 1 = 120
#
# Output:
# Factorial = 120


# Time Complexity: O(n)
# Space Complexity: O(n)
# O(n) because of the recursive call stack.