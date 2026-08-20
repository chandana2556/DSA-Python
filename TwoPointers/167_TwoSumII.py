/*
============================================================
Problem: LeetCode 167 - Two Sum II - Input Array Is Sorted
============================================================

Description:
Given a 1-indexed array of integers numbers that is already
sorted in non-decreasing order, find two numbers such that
their sum is equal to the given target.

Return the indices of the two numbers.

The returned indices must be 1-indexed.

Example:
Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]

Because:
2 + 7 = 9
*/


/*
============================================================
Approach 1: Brute Force
============================================================
Time Complexity  : O(n²)
Space Complexity : O(1)

Try every possible pair of elements.

For each i, check every element after i and see whether
numbers[i] + numbers[j] equals the target.

Time Complexity: O(n²)
Space Complexity: O(1)
*/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        for i in range(n):

            for j in range(i + 1, n):

                if numbers[i] + numbers[j] == target:

                    return [i + 1, j + 1]


/*
============================================================
Approach 2: Two Pointers
============================================================
Time Complexity  : O(n) 
Space Complexity : O(1) 

The array is already sorted, so we can use two pointers.

start → first element
end   → last element

If the sum is greater than target:
    move end to the left.

If the sum is smaller than target:
    move start to the right.

If the sum equals target:
    return the two indices.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal approach.
*/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        start = 0
        end = n - 1

        while start < end:

            s = numbers[start] + numbers[end]

            if s == target:
                return [start + 1, end + 1]

            elif s > target:
                end -= 1

            else:
                start += 1


/*
============================================================
Approach Comparison
============================================================

Why Two Pointers works:
The array is sorted.

If the sum is too large, decrease the right pointer.
If the sum is too small, increase the left pointer.

Therefore, we don't need to check every possible pair.
*/