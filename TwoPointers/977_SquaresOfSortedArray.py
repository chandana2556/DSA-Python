/*
============================================================
Problem: LeetCode 977 - Squares of a Sorted Array
============================================================

Description:
Given an integer array nums sorted in non-decreasing order,
return an array containing the squares of each number,
also sorted in non-decreasing order.

Example:
Input:
nums = [-4, -1, 0, 3, 10]

Output:
[0, 1, 9, 16, 100]
*/


/*
============================================================
Approach 1: Square and Sort
============================================================
Time Complexity  : O(n log n)
Space Complexity : O(n)

First square every element in the array.
Then use Python's sorted() function to sort the squares.

Time Complexity: O(n log n)
Space Complexity: O(n)
*/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        return sorted(nums)


/*
============================================================
Approach 2: Two Pointers
============================================================
Time Complexity  : O(n) 
Space Complexity : O(n)

The input array is already sorted.

The largest square will always come from either:
    - the leftmost negative number, or
    - the rightmost positive number.

Use two pointers:

start → beginning of the array
end   → end of the array

Compare their absolute values.

The larger absolute value produces the larger square,
so place that square at the end of the result array.

We fill the result array from right to left.

Time Complexity: O(n)
Space Complexity: O(n)

This is the optimal approach because we avoid sorting.
*/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)

        start = 0
        end = n - 1

        res = [0] * n

        for i in range(n - 1, -1, -1):

            if abs(nums[start]) > abs(nums[end]):

                res[i] = nums[start] ** 2
                start += 1

            else:

                res[i] = nums[end] ** 2
                end -= 1

        return res


/*
============================================================
Execution Example
============================================================

Input:
nums = [-4, -1, 0, 3, 10]

Compare from both ends:

|-4| = 4
|10| = 10

10² = 100 → place at the end

Then compare:

|-4| = 4
|3| = 3

4² = 16

Continue...

Output:
[0, 1, 9, 16, 100]


Two Pointers is optimal because the input is already sorted,
so we can use the sorted property instead of sorting again.
*/