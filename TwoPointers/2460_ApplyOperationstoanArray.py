/*
============================================================
Problem: LeetCode 2460 - Apply Operations to an Array
============================================================

Description:
Given an integer array nums, perform the following operations
from left to right:

1. If nums[i] == nums[i + 1], multiply nums[i] by 2 and
   set nums[i + 1] to 0.

2. After applying all operations, move all zeroes to the end
   while maintaining the relative order of non-zero elements.

Return the resulting array.

Example:
Input:
nums = [1,2,2,1,1,0]

After operations:
[1,4,0,2,0,0]

After moving zeroes:
[1,4,2,0,0,0]


Edge Cases:
- Empty array
- Single element
- No equal adjacent elements
- All elements are zero
- Consecutive equal elements
*/


/*
============================================================
Approach 1: Extra Array
============================================================

First apply all the required operations.

Then create an extra array and copy all non-zero elements
into it.

The remaining positions stay zero because the new array
is initialized with zeroes.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def applyOperations(self, nums):

        n = len(nums)

        for i in range(n - 1):

            if nums[i] == nums[i + 1]:

                nums[i] *= 2
                nums[i + 1] = 0

        ans = [0] * n

        j = 0

        for i in range(n):

            if nums[i] != 0:

                ans[j] = nums[i]
                j += 1

        return ans


/*
============================================================
Approach 2: Two Pointers - In-Place
============================================================

First apply the required operations.

Then use two pointers:

i → scans through the array
j → position where the next non-zero element should go

Whenever nums[i] is non-zero, place it at nums[j]
and move j forward.

After all non-zero elements are moved to the front,
fill the remaining positions with zeroes.

No extra array is required.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal approach.
*/

class Solution:
    def applyOperations(self, nums):

        n = len(nums)

        for i in range(n - 1):

            if nums[i] == nums[i + 1]:

                nums[i] *= 2
                nums[i + 1] = 0

        j = 0

        for i in range(n):

            if nums[i] != 0:

                nums[j] = nums[i]
                j += 1

        while j < n:

            nums[j] = 0
            j += 1

        return nums


/*
============================================================
Execution Example
============================================================

Input:
nums = [1,2,2,1,1,0]

Step 1: Apply Operations

1 != 2 → no change

2 == 2 → 2 becomes 4
         next element becomes 0

[1,4,0,1,1,0]

1 == 1 → 1 becomes 2
         next element becomes 0

[1,4,0,2,0,0]


Step 2: Move non-zero elements

Non-zero elements:
1, 4, 2

Place them at the beginning:

[1,4,2,_,_,_]

Fill remaining positions with zero:

[1,4,2,0,0,0]

Output:
[1,4,2,0,0,0]

Best Approach:
Two Pointers - In-Place

Reason:
We reuse the original nums array instead of creating
another array, so the extra space is O(1).
*/