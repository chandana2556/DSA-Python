/*
============================================================
Problem: LeetCode 922 - Sort Array By Parity II
============================================================

Description:
Given an array nums containing an equal number of even and
odd integers, rearrange the array so that:

    - Every even index contains an even number.
    - Every odd index contains an odd number.

Return the rearranged array.

The order of the elements does not matter.

Example:
Input:
nums = [4,2,5,7]

Output:
[4,5,2,7]

Index:
0 → even
1 → odd
2 → even
3 → odd


Edge Cases:
- Already correctly arranged array
- All even numbers at wrong positions
- All odd numbers at wrong positions
- Minimum valid array size
*/


/*
============================================================
Approach 1: Separate Even and Odd Arrays
============================================================

Create two lists:

even → stores all even numbers
odd  → stores all odd numbers

Then place one even and one odd alternately into
the result array.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        even = []
        odd = []

        for num in nums:

            if num % 2 == 0:
                even.append(num)

            else:
                odd.append(num)

        result = []

        for i in range(len(even)):

            result.append(even[i])
            result.append(odd[i])

        return result


/*
============================================================
Approach 2: Result Array + Even/Odd Positions
============================================================

Create a result array of the same size.

Use:
    even = 0 → next even position
    odd  = 1 → next odd position

For every number:
    If it is even, place it at the next even index.
    If it is odd, place it at the next odd index.

Move the corresponding pointer by 2.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)

        even = 0
        odd = 1

        for num in nums:

            if num % 2 == 0:

                result[even] = num
                even += 2

            else:

                result[odd] = num
                odd += 2

        return result


/*
============================================================
Approach 3: Two Pointers - In-Place
============================================================

This approach does not use an extra result array.

Use two pointers:

i → checks even indices: 0, 2, 4, ...
j → checks odd indices: 1, 3, 5, ...

For i:
    If nums[i] is already even, move i by 2.

For j:
    If nums[j] is already odd, move j by 2.

If:
    nums[i] is odd
    nums[j] is even

swap them.

After swapping, both positions are correct.

Time Complexity: O(n)
Space Complexity: O(1)

This is the optimal approach because it modifies
the array in-place.
*/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        n = len(nums)

        i = 0
        j = 1

        while i < n and j < n:

            if nums[i] % 2 == 0:

                i += 2

            elif nums[j] % 2 != 0:

                j += 2

            else:

                nums[i], nums[j] = nums[j], nums[i]

                i += 2
                j += 2

        return nums


/*
============================================================
Execution Example
============================================================

Input:
nums = [4,2,5,7]

Even indices:
0 → 4 ✓
2 → 5 ✗

Odd indices:
1 → 2 ✗
3 → 7 ✓

Swap nums[2] and nums[1]:

[4,5,2,7]

Now:
index 0 → 4 → even ✓
index 1 → 5 → odd ✓
index 2 → 2 → even ✓
index 3 → 7 → odd ✓

*/