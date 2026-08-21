/*
============================================================
Problem: LeetCode 75 - Sort Colors
============================================================

Description:
Given an array nums containing only 0, 1, and 2,
sort the array in-place so that all 0s come first,
followed by all 1s, followed by all 2s.

Do not use the library sorting function in the
optimal approach.

Example:
Input:
nums = [2,0,2,1,1,0]

Output:
[0,0,1,1,2,2]

Edge Cases:
- All elements are the same
- Only one element
- Already sorted array
- Reverse sorted array
*/


/*
============================================================
Approach 1: Built-in Sorting
============================================================

Use Python's built-in sort() function.

Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space
*/

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        nums.sort()


/*
============================================================
Approach 2: Counting
============================================================

Since the array contains only 0, 1, and 2,
count how many times each value occurs.

Then overwrite the array with:
    count0 number of 0s
    count1 number of 1s
    count2 number of 2s

Time Complexity: O(n)
Space Complexity: O(1)
*/


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count0 = 0
        count1 = 0
        count2 = 0

        for num in nums:

            if num == 0:
                count0 += 1

            elif num == 1:
                count1 += 1

            else:
                count2 += 1

        i = 0

        for _ in range(count0):
            nums[i] = 0
            i += 1

        for _ in range(count1):
            nums[i] = 1
            i += 1

        for _ in range(count2):
            nums[i] = 2
            i += 1


/*
============================================================
Approach 3: Dutch National Flag Algorithm
============================================================

Use three pointers:

start → position where the next 0 should go
mid   → current element being checked
end   → position where the next 2 should go

Rules:

If nums[mid] == 0:
    Swap with start.
    Move start and mid forward.

If nums[mid] == 1:
    It is already in the correct region.
    Move mid forward.

If nums[mid] == 2:
    Swap with end.
    Move end backward.

Important:
After swapping with end, do NOT move mid,
because the element coming from the end
has not been checked yet.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal approach.
*/


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        start = 0
        mid = 0
        end = len(nums) - 1

        while mid <= end:

            if nums[mid] == 1:

                mid += 1

            elif nums[mid] == 0:

                nums[start], nums[mid] = nums[mid], nums[start]

                start += 1
                mid += 1

            else:

                nums[end], nums[mid] = nums[mid], nums[end]

                end -= 1


/*
============================================================
Execution Example
============================================================

Input:
nums = [2,0,2,1,1,0]

Initially:

start = 0
mid   = 0
end   = 5

The algorithm divides the array into regions:

[0s] [unknown] [1s] [2s]

At the end:

[0,0,1,1,2,2]


============================================================
Approach Comparison
============================================================

The Dutch National Flag algorithm is the preferred
interview solution because it sorts the array in one pass
using constant extra space.
*/