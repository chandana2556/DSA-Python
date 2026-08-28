/*
============================================================
Problem: LeetCode 80 - Remove Duplicates from Sorted Array II
============================================================

Description:
Given a sorted integer array nums, remove duplicates in-place
such that each unique element appears at most twice.

Return k, the number of elements remaining after removing
the extra duplicates.

The first k elements of nums should contain the valid elements
in sorted order.

Example:
Input:
nums = [1,1,1,2,2,3]

Output:
k = 5

First 5 elements:
[1,1,2,2,3]

Edge Cases:
- Empty array
- Single element
- Every element appears at most twice
- All elements are the same
- Some elements appear more than twice
*/


/*
============================================================
Approach 1: Extra Array + Counting
============================================================

Since the array is sorted, duplicate elements are adjacent.

Count how many times each element occurs.

Only the first two occurrences of each element are stored
in the temporary array.

Finally, copy the valid elements back into nums.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)

        res = [0] * n
        j = 0
        count = 0

        for i in range(n):

            if i == 0 or nums[i] != nums[i - 1]:
                count = 1
            else:
                count += 1

            if count <= 2:
                res[j] = nums[i]
                j += 1

        for i in range(j):
            nums[i] = res[i]

        return j


/*
============================================================
Approach 2: Using a Frequency Dictionary
============================================================

Since the array is sorted, we can count the occurrences
of each number.

For every number, allow it to be added only when its
frequency is less than or equal to 2.

Store the valid elements in a temporary array and then
copy them back into nums.

Time Complexity: O(n)
Space Complexity: O(n)

This approach is mainly useful for understanding the
"allow at most twice" condition.
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        frequency = {}
        res = []

        for num in nums:

            frequency[num] = frequency.get(num, 0) + 1

            if frequency[num] <= 2:
                res.append(num)

        for i in range(len(res)):
            nums[i] = res[i]

        return len(res)


/*
============================================================
Approach 3: Two Pointers - In-Place
============================================================

This is the optimal approach.

Because the array is sorted, the first two elements are
always allowed.

Start j from index 2.

For every element nums[i], compare it with nums[j - 2].

If they are different:
    nums[i] can be included.

If they are the same:
    there are already two copies of that value in the
    valid portion, so skip it.

Why j - 2?

We allow each number to appear at most twice.

Time Complexity: O(n)
Space Complexity: O(1)

This is the best approach.
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)

        j = 2

        for i in range(2, n):

            if nums[i] != nums[j - 2]:

                nums[j] = nums[i]
                j += 1

        return j


/*
============================================================
Execution Example
============================================================

Input:
nums = [1,1,1,2,2,3]

First two elements are always allowed:

[1,1]

j = 2

i = 2:
nums[i] = 1
nums[j-2] = nums[0] = 1

Same → skip


i = 3:
nums[i] = 2
nums[j-2] = nums[0] = 1

Different → keep

[1,1,2]


i = 4:
nums[i] = 2
nums[j-2] = nums[1] = 1

Different → keep

[1,1,2,2]


i = 5:
nums[i] = 3
nums[j-2] = nums[2] = 2

Different → keep

[1,1,2,2,3]

Return:
5

Best Approach:
Two Pointers

Reason:
The array is already sorted, so we don't need a HashMap,
Set, or extra array.

We simply compare nums[i] with nums[j - 2] to make sure
that no value appears more than twice.
*/