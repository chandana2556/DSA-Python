# ============================================================
# RECURSION BASICS
# ============================================================


# ============================================================
# 1. Print Numbers from 1 to N
# ============================================================

# Iterative Approach

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')

print_numbers(5)

# Time Complexity: O(n)
# Space Complexity: O(1)


# Recursive Approach

def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=' ')

print_numbers(5)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Reason: Recursive call stack


# ============================================================
# 2. Print Numbers from N to 1
# ============================================================

# Iterative Approach

def print_reverse(n):
    for i in range(n, 0, -1):
        print(i, end=' ')

print_reverse(5)

# Time Complexity: O(n)
# Space Complexity: O(1)


# Recursive Approach

def print_reverse(n):
    if n == 0:
        return

    print(n, end=' ')
    print_reverse(n - 1)

print_reverse(5)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Reason: Recursive call stack


# ============================================================
# 3. Find Sum of First N Numbers
# ============================================================

# Iterative Approach

def sum_numbers(n):
    sum_ = 0

    for i in range(1, n + 1):
        sum_ = sum_ + i

    return sum_

print(sum_numbers(5))

# Time Complexity: O(n)
# Space Complexity: O(1)


# Recursive Approach

def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)

print(sum_numbers(5))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Reason: Recursive call stack


# ============================================================
# 4. Find Power of a Number
# ============================================================

def power_num(a, n):

    if n == 0:
        return 1

    return a * power_num(a, n - 1)

print(power_num(2, 5))

# Time Complexity: O(n)
# Space Complexity: O(n)
# Reason: Recursive call stack