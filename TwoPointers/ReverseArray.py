# Problem: Reverse an Array

# Description:
# Given an array arr, reverse the elements of the array
# in-place.
#
# The first element should become the last element,
# the second element should become the second-last element,
# and so on.
#
# The original array should be modified directly.
#
# ============================================================
# Edge Cases:
# ============================================================
#
# - Empty array
# - Single element
# - Even number of elements
# - Odd number of elements
#
# ============================================================
# Approach 1: Using Index
# ============================================================

class Solution:
    def reverseArray(self, arr):

        n = len(arr)

        for i in range(n // 2):

            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


# Time Complexity: O(n)
# Space Complexity: O(1)


# ============================================================
# Approach 2: Two Pointers
# ============================================================

class Solution:
    def reverseArray(self, arr):

        left = 0
        right = len(arr) - 1

        while left < right:

            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1


# Time Complexity: O(n)
# Space Complexity: O(1)


# ============================================================
# Key Idea:
# ============================================================
#
# Use two positions:
#
# left  → starts from the beginning
# right → starts from the end
#
# Swap arr[left] and arr[right].
#
# Then:
#
# left  → move forward
# right → move backward
#
# Continue until left >= right.
#
# Both approaches reverse the array in-place,
# so no extra array is required.