/*
============================================================
Problem: LeetCode 283 - Move Zeroes
============================================================

Description:
Given an integer array nums, move all 0s to the end of the
array while maintaining the relative order of all non-zero
elements.

The operation must be performed in-place.

Example:
Input:
nums = [0,1,0,3,12]

Output:
[1,3,12,0,0]

Edge Cases:
- No zeroes
- All zeroes
- Single element
- Zero at the beginning
- Zero at the end
*/


/*
============================================================
Approach 1: Extra Array
============================================================

Create a new array.

First store all non-zero elements.
Then fill the remaining positions with zeroes.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        result = []

        for num in nums:

            if num != 0:
                result.append(num)

        while len(result) < len(nums):

            result.append(0)

        for i in range(len(nums)):

            nums[i] = result[i]


/*
============================================================
Approach 2: Two Pointers - Swap
============================================================

Use two pointers:

j → position where the next non-zero element should go
i → scans through the array

Whenever nums[i] is non-zero, swap it with nums[j]
and move j forward.

This automatically moves zeroes towards the end while
maintaining the relative order of non-zero elements.

Time Complexity: O(n)
Space Complexity: O(1)
*/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[i], nums[j] = nums[j], nums[i]

                j += 1


/*
============================================================
Approach 3: Two Pointers - Overwrite
============================================================

First copy all non-zero elements to the beginning of
the same array.

Then fill the remaining positions with zeroes.

This avoids unnecessary swaps when there are many zeroes.

Time Complexity: O(n)
Space Complexity: O(1)
*/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[j] = nums[i]

                j += 1

        while j < len(nums):

            nums[j] = 0

            j += 1


/*
============================================================
Execution Example
============================================================

Input:
nums = [0,1,0,3,12]

Using the two-pointer approach:

j = 0

i = 0 → nums[0] = 0
        skip

i = 1 → nums[1] = 1
        place 1 at index 0
        j = 1

i = 2 → nums[2] = 0
        skip

i = 3 → nums[3] = 3
        place 3 at index 1
        j = 2

i = 4 → nums[4] = 12
        place 12 at index 2
        j = 3

Final:

[1,3,12,0,0]


============================================================
Approach Comparison
============================================================

The two-pointer approaches are preferred because they
modify the array in-place without using an extra array.
*/