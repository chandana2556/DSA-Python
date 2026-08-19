# Problem: LeetCode 509 - Fibonacci Number
#
# Description:
# Given an integer n, return the nth Fibonacci number.
#
# Fibonacci sequence:
# 0, 1, 1, 2, 3, 5, 8, ...
#
# Formula:
# F(n) = F(n-1) + F(n-2)


# =======================
# Approach 1: Iterative
# =======================

class Solution:
    def fib(self, n: int) -> int:
        n1, n2 = 0, 1

        for i in range(n):
            n3 = n1 + n2
            n1, n2 = n2, n3

        return n1

# Time Complexity: O(n)
# Space Complexity: O(1)


# =======================
# Approach 2: Recursion
# =======================

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

# Time Complexity: O(2^n)
# Space Complexity: O(n)


# =======================
# Approach 3: Dynamic Programming
# =======================

class Solution:
    def fib(self, n: int) -> int:
        f = [0] * (n + 1)

        if n == 0:
            return 0

        elif n == 1:
            return 1

        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]

# Time Complexity: O(n)
# Space Complexity: O(n)