/*
============================================================
Problem: LeetCode 27 - Remove Element
============================================================

Description:
Given an integer array nums and an integer val, remove all
occurrences of val in-place.

The order of the remaining elements may be changed.

Return k, the number of elements in nums that are not equal
to val.

The first k elements of nums should contain the elements
that are not equal to val.

Example:
Input:
nums = [3,2,2,3]
val = 3

Output:
k = 2

First 2 elements:
[2,2]


Edge Cases:
- Empty array
- val does not exist
- All elements are val
- No elements are val
*/


/*
============================================================
Approach 1: Extra Array
============================================================

Create a new list and store only the elements that are
different from val.

Then copy those elements back into nums.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        result = []

        for num in nums:

            if num != val:
                result.append(num)

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)


/*
============================================================
Approach 2: Two Pointers - Overwrite
============================================================

Use two pointers:

i → scans through the array
j → position where the next valid element should be placed

If nums[i] is not equal to val:

    nums[j] = nums[i]
    j += 1

Elements equal to val are simply skipped.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal approach.
*/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)

        j = 0

        for i in range(n):

            if nums[i] != val:

                nums[j] = nums[i]
                j += 1

        return j


/*
============================================================
Approach 3: Two Pointers - Swap from End
============================================================

Since the order of the remaining elements does not matter,
when nums[i] equals val, replace it with an element from
the end of the array.

This can reduce the number of assignments when many
elements equal val.

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        n = len(nums)

        while i < n:

            if nums[i] == val:

                nums[i] = nums[n - 1]
                n -= 1

            else:

                i += 1

        return n


/*
============================================================
Execution Example
============================================================

Input:
nums = [3,2,2,3]
val = 3

Using the overwrite approach:

i = 0 → nums[0] = 3
        equal to val → skip

i = 1 → nums[1] = 2
        nums[0] = 2
        j = 1

i = 2 → nums[2] = 2
        nums[1] = 2
        j = 2

i = 3 → nums[3] = 3
        equal to val → skip

Return:
2

First 2 elements:
[2,2]

*/