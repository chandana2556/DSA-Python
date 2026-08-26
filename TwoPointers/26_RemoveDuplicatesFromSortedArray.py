/*
============================================================
Problem: LeetCode 26 - Remove Duplicates from Sorted Array
============================================================

Description:
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once.

Return the number of unique elements.

The first k elements of nums should contain the unique
elements in sorted order.

Example:
Input:
nums = [1,1,2,2,3]

Output:
k = 3

First 3 elements:
[1,2,3]


Edge Cases:
- Empty array
- Single element
- All elements are unique
- All elements are duplicates
*/


/*
============================================================
Approach 1: Using Set
============================================================

Since the array is already sorted, we can use a set to
store unique elements.

Then copy the unique elements back into nums.

Time Complexity: O(n)
Space Complexity: O(n)

This approach is simple but uses extra space.
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique = set(nums)

        unique = sorted(unique)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)


/*
============================================================
Approach 2: Using a New List
============================================================

Create a new list and add an element only when it is
different from the previous element.

Since nums is sorted, duplicates will always be next
to each other.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique = []

        for num in nums:

            if len(unique) == 0 or unique[-1] != num:
                unique.append(num)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)


/*
============================================================
Approach 3: Two Pointers - In-Place
============================================================

This is the optimal approach.

Use two pointers:

i → scans through the array
j → position of the last unique element

Whenever nums[i] is different from nums[j]:

    Move j forward.
    Copy nums[i] to nums[j].

Because the array is sorted, duplicates are adjacent.

No extra array or data structure is required.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal solution.
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0

        j = 0

        for i in range(1, n):

            if nums[i] != nums[j]:

                j += 1
                nums[j] = nums[i]

        return j + 1


/*
============================================================
Execution Example
============================================================

Input:
nums = [1,1,2,2,3]

Initially:
j = 0

i = 1:
nums[1] == nums[0]
duplicate → skip

i = 2:
nums[2] != nums[0]
j = 1
nums[1] = nums[2]

Array:
[1,2,2,2,3]

i = 3:
nums[3] == nums[1]
duplicate → skip

i = 4:
nums[4] != nums[1]
j = 2
nums[2] = nums[4]

Array:
[1,2,3,2,3]

Return:
j + 1 = 3

First 3 elements:
[1,2,3]

*/