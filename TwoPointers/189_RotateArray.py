/*
============================================================
Problem: LeetCode 189 - Rotate Array
============================================================

Description:
Given an integer array nums, rotate the array to the right
by k steps.

A right rotation by one step moves the last element to the
first position.

Since k can be larger than the length of the array, we use:

k = k % n..

to reduce unnecessary rotations.

Example:
Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]


Edge Cases:
- k = 0
- k is greater than n
- k is equal to n
- Array contains one element
- Empty array
*/


/*
============================================================
Approach 1: Rotate One Step at a Time
============================================================

Perform a single right rotation k times.

For each rotation:
    1. Store the last element.
    2. Shift every other element one position to the right.
    3. Put the last element at index 0.

Time Complexity: O(n * k)
Space Complexity: O(1)

This is the brute-force approach.
*/

class Solution:
    def rotate(self, nums, k):

        n = len(nums)

        if n == 0:
            return

        k = k % n

        for _ in range(k):

            last = nums[n - 1]

            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = last


/*
============================================================
Approach 2: Extra Result Array
============================================================

Create a new array of the same size.

For every element at index i, its new position after
rotating right by k positions is:

new_index = (i + k) % n

Place each element at its new index.

Finally, copy the result back into nums.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def rotate(self, nums, k):

        n = len(nums)

        if n == 0:
            return

        k = k % n

        result = [0] * n

        for i in range(n):

            new_index = (i + k) % n

            result[new_index] = nums[i]

        for i in range(n):

            nums[i] = result[i]


/*
============================================================
Approach 3: Python Slicing
============================================================

Take the last k elements and place them before the
remaining elements.

nums[-k:] → last k elements
nums[:-k] → remaining elements

Then combine them:

last k elements + remaining elements

This is the shortest Python solution.

Time Complexity: O(n)
Space Complexity: O(n)

Note:
This approach is simple but uses extra memory because
slicing creates new lists.
*/

class Solution:
    def rotate(self, nums, k):

        n = len(nums)

        if n == 0:
            return

        k = k % n

        if k == 0:
            return

        nums[:] = nums[-k:] + nums[:-k]


/*
============================================================
Approach 4: Reversal Algorithm
============================================================

This is the optimal and most commonly expected approach.

For right rotation by k:

Step 1:
Reverse the entire array.

Step 2:
Reverse the first k elements.

Step 3:
Reverse the remaining n-k elements.

Why it works:

Original:
[1,2,3,4,5,6,7]

k = 3

Reverse entire array:
[7,6,5,4,3,2,1]

Reverse first 3:
[5,6,7,4,3,2,1]

Reverse remaining:
[5,6,7,1,2,3,4]

Time Complexity: O(n)
Space Complexity: O(1)

This is the preferred interview approach.
*/

class Solution:
    def rotate(self, nums, k):

        n = len(nums)

        if n == 0:
            return

        k = k % n

        self.reverse(nums, 0, n - 1)

        self.reverse(nums, 0, k - 1)

        self.reverse(nums, k, n - 1)

    def reverse(self, nums, left, right):

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1


/*
============================================================
Approach 5: Cyclic Replacement
============================================================

Instead of reversing the array, move each element directly
to its final position.

For an element at index current:

    next_index = (current + k) % n

Move the current element to next_index.

The displaced element is then moved to its correct position.

Continue until we return to the starting index.

If one cycle does not cover the entire array, start another
cycle from the next index.

The count variable keeps track of how many elements have
been moved.

Time Complexity: O(n)
Space Complexity: O(1)

This is also an optimal in-place approach, but it is more
complex than the reversal method.
*/

class Solution:
    def rotate(self, nums, k):

        n = len(nums)

        if n == 0:
            return

        k = k % n

        if k == 0:
            return

        count = 0
        start = 0

        while count < n:

            current = start
            prev = nums[current]

            while True:

                next_index = (current + k) % n

                nums[next_index], prev = prev, nums[next_index]

                current = next_index
                count += 1

                if current == start:
                    break

            start += 1


/*
============================================================
Execution Example
============================================================

Input:
nums = [1,2,3,4,5,6,7]
k = 3


Approach 1:

Rotate once:
[7,1,2,3,4,5,6]

Rotate twice:
[6,7,1,2,3,4,5]

Rotate three times:
[5,6,7,1,2,3,4]


Approach 2:

For each element:

1 → index (0 + 3) % 7 = 3
2 → index (1 + 3) % 7 = 4
3 → index (2 + 3) % 7 = 5
4 → index (3 + 3) % 7 = 6
5 → index (4 + 3) % 7 = 0
6 → index (5 + 3) % 7 = 1
7 → index (6 + 3) % 7 = 2

Result:
[5,6,7,1,2,3,4]


Approach 4:

Original:
[1,2,3,4,5,6,7]

Reverse entire:
[7,6,5,4,3,2,1]

Reverse first 3:
[5,6,7,4,3,2,1]

Reverse remaining:
[5,6,7,1,2,3,4]


============================================================
Approach Comparison
============================================================

Approach 1: One-Step Rotation
Time  : O(n * k)
Space : O(1)

Approach 2: Extra Result Array
Time  : O(n)
Space : O(n)

Approach 3: Slicing
Time  : O(n)
Space : O(n)

Approach 4: Reversal Algorithm
Time  : O(n) ⭐
Space : O(1) ⭐

Approach 5: Cyclic Replacement
Time  : O(n) ⭐
Space : O(1) ⭐


============================================================
Best Approach
============================================================

Reversal Algorithm is generally the best choice for
interviews.

Why?

- O(n) time
- O(1) extra space
- Simple once the pattern is understood
- Works in-place
- Does not require an extra array


Important Formula:

k = k % n

This handles cases where k is greater than the array length.
*/
