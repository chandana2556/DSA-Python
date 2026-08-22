/*
============================================================
Problem: LeetCode 2164 - Sort Even and Odd Indices
Independently
============================================================

Description:
Given an integer array nums:

1. Elements at even indices must be sorted in increasing order.
2. Elements at odd indices must be sorted in decreasing order.

The elements must remain at their respective parity indices.

Example:
Input:
nums = [4,1,2,3]

Even indices:
0, 2 → [4,2] → [2,4]

Odd indices:
1, 3 → [1,3] → [3,1]

Output:
[2,3,4,1]


Edge Cases:
- Single element
- Only even indices
- Array with all equal elements
- Already sorted array
*/


/*
============================================================
Approach 1: Slicing + Sorting
============================================================

nums[::2] selects elements at even indices.
nums[1::2] selects elements at odd indices.

Sort even-indexed elements in ascending order.

Sort odd-indexed elements in descending order.

The sorted values are directly assigned back using slicing.

Time Complexity: O(n log n)
Space Complexity: O(n)

This is the shortest Python approach.
*/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        nums[::2] = sorted(nums[::2])

        nums[1::2] = sorted(nums[1::2], reverse=True)

        return nums


/*
============================================================
Approach 2: Separate Even and Odd Arrays
============================================================

First extract the elements at even and odd indices.

Then:
    even → sort in ascending order
    odd  → sort in descending order

Finally place them back into their original parity indices.

Time Complexity: O(n log n)
Space Complexity: O(n)
*/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        even = sorted(nums[::2])

        odd = sorted(nums[1::2], reverse=True)

        for i in range(len(even)):
            nums[2 * i] = even[i]

        for i in range(len(odd)):
            nums[2 * i + 1] = odd[i]

        return nums


/*
============================================================
Approach 3: Separate + Sort + Two Indexes
============================================================

Create two lists:

even → elements from even indices
odd  → elements from odd indices

Sort:
    even → ascending
    odd  → descending

Use two indexes i and j to take elements from the
sorted even and odd arrays.

Then place them back into nums.

Time Complexity: O(n log n)
Space Complexity: O(n)

This approach is more explicit and beginner-friendly
because every step is clearly visible.
*/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        even = []
        odd = []
        n = len(nums)

        for i in range(n):

            if i % 2 == 0:
                even.append(nums[i])

            else:
                odd.append(nums[i])

        even.sort()
        odd.sort(reverse=True)

        i = 0
        j = 0

        for k in range(n):

            if k % 2 == 0:
                nums[k] = even[i]
                i += 1

            else:
                nums[k] = odd[j]
                j += 1

        return nums


/*
============================================================
Execution Example
============================================================

Input:
nums = [4,1,2,3]

Even indices:
index 0 → 4
index 2 → 2

even = [4,2]
sorted → [2,4]


Odd indices:
index 1 → 1
index 3 → 3

odd = [1,3]
reverse sorted → [3,1]


Place them back:

index 0 → 2
index 1 → 3
index 2 → 4
index 3 → 1

Output:
[2,3,4,1]


