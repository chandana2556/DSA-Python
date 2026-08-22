/*
============================================================
Problem: LeetCode 905 - Sort Array By Parity
============================================================

Description:
Given an integer array nums, move all even integers to the
beginning of the array followed by all odd integers.

The relative order of the elements does not matter.

Example:
Input:
nums = [3,1,2,4]

Output:
[2,4,3,1]

Any arrangement with all even numbers before all odd
numbers is valid.

Edge Cases:
- Empty array
- Single element
- All even numbers
- All odd numbers
- Mix of even and odd numbers
*/


/*
============================================================
Approach 1: Using sort() with key
============================================================

Python's sort() can sort elements based on a key.

For every number:
    even → x % 2 = 0
    odd  → x % 2 = 1

So sorting by x % 2 places all even numbers first
and odd numbers after them.

lambda x: x % 2
means:
    take x
    return x % 2
    use this value as the sorting key.

Time Complexity: O(n log n)
Space Complexity: O(n)
*/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        nums.sort(key=lambda x: x % 2)

        return nums


/*
============================================================
Approach 2: Two Pointers
============================================================

Use j to represent the position where the next even number
should be placed.

i scans through the array.

If nums[i] is even:
    swap nums[i] with nums[j]
    move j forward.

This places all even numbers at the beginning.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal in-place approach.
*/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        j = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 0:

                nums[i], nums[j] = nums[j], nums[i]

                j += 1

        return nums


/*
============================================================
Approach 3: Extra Arrays
============================================================

Create two separate lists:

even → stores even numbers
odd  → stores odd numbers

Finally combine them:

even + odd

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        even = []
        odd = []

        for num in nums:

            if num % 2 == 0:
                even.append(num)

            else:
                odd.append(num)

        return even + odd


/*
============================================================
Execution Example
============================================================

Input:
nums = [3,1,2,4]

Approach 1:
Sorting based on x % 2

3 % 2 = 1
1 % 2 = 1
2 % 2 = 0
4 % 2 = 0

Output:
[2,4,3,1]


Approach 2:
Two pointers place even numbers at the beginning.

Output:
[2,4,3,1]


Approach 3:
even = [2,4]
odd  = [3,1]

even + odd

Output:
[2,4,3,1]
