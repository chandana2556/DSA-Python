# Problem: LeetCode 70 - Climbing Stairs
#
# Description:
# You are climbing a staircase with n steps.
# At each step, you can climb either 1 step or 2 steps.
#
# Return the number of distinct ways to reach the top.
#
# Key Observation:
# This problem follows the Fibonacci pattern.
#
# For n = 1:
# Number of ways = 1
# Fibonacci(2) = 1
#
# For n = 2:
# Number of ways = 2
# Fibonacci(3) = 2
#
# For n = 3:
# Number of ways = 3
# Fibonacci(4) = 3
#
# For n = 4:
# Number of ways = 5
# Fibonacci(5) = 5
#
# Therefore:
#
# Number of ways to climb n stairs
# = Fibonacci(n + 1)
#
# So instead of solving Climbing Stairs separately,
# we can calculate Fibonacci(n + 1).


# =======================
# Approach 1: Recursion
# =======================

class Solution:

    def fib(self, n):
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    def climbStairs(self, n: int) -> int:
        return self.fib(n + 1)

# Time Complexity: O(2^n)
# Space Complexity: O(n)


# =======================
# Approach 2: Dynamic Programming
# =======================

class Solution:

    def fib(self, n):
        f = [0] * (n + 1)

        if n <= 1:
            f[n] = n
        else:
            f[0] = 0
            f[1] = 1

            for i in range(2, n + 1):
                f[i] = f[i - 1] + f[i - 2]

        return f[n]

    def climbStairs(self, n: int) -> int:
        return self.fib(n + 1)

# Time Complexity: O(n)
# Space Complexity: O(n)


# =======================
# Execution Example
# =======================
#
# Input:
# n = 4
#
# We calculate:
#
# fib(n + 1)
# = fib(5)
#
# Fibonacci sequence:
#
# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
#
# Therefore:
#
# Output = 5
#
#
# Ways to climb 4 stairs:
#
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2
#
# Total = 5


# =======================
# Important Pattern
# =======================
#
# Climbing Stairs:
#
# ways(n) = ways(n-1) + ways(n-2)
#
# Fibonacci:
#
# F(n) = F(n-1) + F(n-2)
#
# The only difference is the starting position.
#
# Fibonacci:
# F(0) = 0
# F(1) = 1
#
# Climbing Stairs:
# ways(1) = 1 = F(2)
# ways(2) = 2 = F(3)
#
# Therefore:
#
# ways(n) = F(n + 1)
#
# This is why we call:
#
# self.fib(n + 1)