# ============================================================
# Problem: LeetCode 238 - Product of Array Except Self
# ============================================================
#
# Description:
# Given an integer array nums, return an array answer
# such that answer[i] is equal to the product of all
# elements of nums except nums[i].
#
# Do not use division.
#
# Example:
# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
#
# Edge Cases:
# - Array contains zero
# - Array contains multiple zeros
# - Negative numbers
# - Single element
#
# ============================================================
# Approach 1: Brute Force
# ============================================================

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []

        for i in range(n):

            product = 1

            for j in range(n):

                if i != j:
                    product = product * nums[j]

            result.append(product)

        return result


# Time Complexity: O(n²)
# Space Complexity: O(n)
# O(n) for the result array.


# ============================================================
# Approach 2: Prefix and Suffix Arrays
# ============================================================

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        # Store product of elements before each index
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Store product of elements after each index
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Combine prefix and suffix products
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result


# Time Complexity: O(n)
# Space Complexity: O(n)
# Extra space is used for prefix, suffix and result arrays.


# ============================================================
# Approach 3: Prefix + Running Suffix
# Optimal Approach
# ============================================================

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        result = [1] * n

        # Store prefix products directly in result
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Calculate suffix product while moving backwards
        suffixProduct = 1

        for i in range(n - 1, -1, -1):

            result[i] = result[i] * suffixProduct

            suffixProduct = suffixProduct * nums[i]

        return result


# Time Complexity: O(n)
# Space Complexity: O(1)
# Extra space is O(1), excluding the output array.


# ============================================================
# Approach Comparison
# ============================================================
#
# Approach 1: Brute Force
# Time  : O(n²)
# Space : O(n)
#
# Approach 2: Prefix + Suffix Arrays
# Time  : O(n)
# Space : O(n)
#
# Approach 3: Prefix + Running Suffix
# Time  : O(n)
# Space : O(1) ⭐
#
# Approach 3 is optimal because we reuse the result array
# for storing prefix products and use only one variable
# (suffixProduct) for the suffix product.
#
# ============================================================