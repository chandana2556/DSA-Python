/*
============================================================
Problem: LeetCode 1470 - Shuffle the Array
============================================================

Description:
Given an array nums consisting of 2n elements in the form:

[x1, x2, ..., xn, y1, y2, ..., yn]

Return the array in the shuffled form:

[x1, y1, x2, y2, ..., xn, yn]

The first half contains the x values and the second half.
contains the y values.

Example:
Input:
nums = [2,5,1,3,4,7]
n = 3

Output:
[2,3,5,4,1,7]


Edge Cases:
- n = 1
- Minimum valid array
- All elements are the same
- Negative values
*/


/*
============================================================
Approach 1: Two Pointers
============================================================

Use two pointers:

i → starts from the beginning of the first half
j → starts from the beginning of the second half

For every iteration:
    Add nums[i]
    Add nums[j]

Then move both pointers forward.

This directly follows the structure of the input array.

Time Complexity: O(n)
Space Complexity: O(n)

Space is O(n) because we create a result list.
*/

class Solution:
    def shuffle(self, nums, n):

        result = []

        i = 0
        j = n

        while i < n:

            result.append(nums[i])
            result.append(nums[j])

            i += 1
            j += 1

        return result


/*
============================================================
Approach 2: Single Loop
============================================================

Instead of maintaining two pointers, use one loop.

For every i from 0 to n-1:

    nums[i]     → x[i]
    nums[i+n]   → y[i]

Append them alternately to the result.

Time Complexity: O(n)
Space Complexity: O(n)

This is simpler than the two-pointer approach.
*/

class Solution:
    def shuffle(self, nums, n):

        result = []

        for i in range(n):

            result.append(nums[i])
            result.append(nums[i + n])

        return result


/*
============================================================
Approach 3: List Comprehension
============================================================

Use Python's list comprehension to perform the same
interleaving operation in a compact way.

For every i:
    take nums[i]
    then take nums[i+n]

The values are added alternately to the result list.

Time Complexity: O(n)
Space Complexity: O(n)

This is the shortest and most Pythonic approach.
*/

class Solution:
    def shuffle(self, nums, n):

        return [value
                for i in range(n)
                for value in (nums[i], nums[i + n])]


/*
============================================================
Approach 4: Slicing + Zip
============================================================

Split the array into two parts:

x = first n elements
y = remaining n elements

Then use zip() to pair corresponding elements:

(x1, y1)
(x2, y2)
...

Append each pair alternately into the result.

Time Complexity: O(n)
Space Complexity: O(n)

Extra space is used for x, y, and result.
*/

class Solution:
    def shuffle(self, nums, n):

        x = nums[:n]
        y = nums[n:]

        result = []

        for a, b in zip(x, y):

            result.append(a)
            result.append(b)

        return result


/*
============================================================
Approach 5: In-Place Encoding
============================================================

This approach tries to avoid creating an extra result array.

Since the constraints allow the values to be encoded using
a multiplier m, we temporarily store two values inside
one integer.

m = 1001

For every i:

    nums[i] = x + y * m

The original x can be recovered using:

    x = nums[i] % m

The y value can be recovered using:

    y = nums[i] // m

After encoding all elements, traverse from right to left
and place x and y at their final positions.

Traversing from right to left prevents overwriting values
that are still required.

Time Complexity: O(n)
Space Complexity: O(1)

This is the most space-efficient approach.
*/

class Solution:
    def shuffle(self, nums, n):

        m = 1001

        for i in range(n):

            nums[i] = nums[i] + (nums[i + n] % m) * m

        for i in range(n - 1, -1, -1):

            y = nums[i] // m
            x = nums[i] % m

            nums[2 * i] = x
            nums[2 * i + 1] = y

        return nums


/*
============================================================
Execution Example
============================================================

Input:
nums = [2,5,1,3,4,7]
n = 3

First half:
[2,5,1]

Second half:
[3,4,7]

Pair the corresponding elements:

2 → 3
5 → 4
1 → 7

Result:

[2,3,5,4,1,7]


============================================================
Approach Comparison
============================================================

Approach 1: Two Pointers
Time  : O(n)
Space : O(n)

Approach 2: Single Loop
Time  : O(n)
Space : O(n)

Approach 3: List Comprehension
Time  : O(n)
Space : O(n)

Approach 4: Slicing + Zip
Time  : O(n)
Space : O(n)

Approach 5: In-Place Encoding
Time  : O(n)
Space : O(1) 


The first four approaches create a result list, so they
use O(n) extra space.

The fifth approach modifies nums directly and uses O(1)
extra space.
*/
