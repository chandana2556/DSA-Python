"""
============================================================
Problem: LeetCode 1422 - Maximum Score After Splitting a String

Description:
Given a binary string s, split it into two non-empty
substrings, left and right.

Calculate the score for each split:
    Score = Number of 0s in left + Number of 1s in right

Return the maximum possible score.

Concept:
The problem uses string manipulation, prefix sums, and
running counts.

Example:
Input:
s = "00111"

Output:
5

Explanation:
Split: "00" | "111"

Zeros in left = 2
Ones in right = 3

Score = 2 + 3 = 5
============================================================
"""


"""
============================================================
Approach 1: Brute Force

- Try every possible split position.
- Create left and right substrings.
- Count zeros in the left substring.
- Count ones in the right substring.
- Calculate the score and update max_score.

Time Complexity: O(n^2)
Space Complexity: O(n)
============================================================
"""

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            count_left = 0
            count_right = 0

            for j in range(len(left)):
                if left[j] == '0':
                    count_left += 1

            for j in range(len(right)):
                if right[j] == '1':
                    count_right += 1

            score = count_left + count_right
            max_score = max(max_score, score)

        return max_score


"""
============================================================
Approach 2: Prefix Sum Arrays

Concept:
- zero_prefix[i] stores the number of zeros from the
  beginning through index i.
- one_suffix[i] stores the number of ones from index i
  to the end.
- Try every valid split and calculate the score using
  zero_prefix[i] + one_suffix[i + 1].

Time Complexity: O(n)
Space Complexity: O(n)
============================================================
"""

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        zero_prefix = [0] * n
        one_suffix = [0] * n

        zero_prefix[0] = 1 if s[0] == '0' else 0

        for i in range(1, n):
            zero_prefix[i] = zero_prefix[i - 1]

            if s[i] == '0':
                zero_prefix[i] += 1

        one_suffix[n - 1] = 1 if s[n - 1] == '1' else 0

        for i in range(n - 2, -1, -1):
            one_suffix[i] = one_suffix[i + 1]

            if s[i] == '1':
                one_suffix[i] += 1

        max_score = 0

        for i in range(n - 1):
            score = zero_prefix[i] + one_suffix[i + 1]
            max_score = max(max_score, score)

        return max_score


"""
============================================================
Approach 3: Running Count - Optimal

Concept:
- First count all the ones in the string.
- Initially, all ones belong to the right substring.
- Move the split from left to right.
- If the current character is '0', increment count_left.
- Otherwise, decrement count_right.
- Calculate the score at every valid split and update
  max_score.

No substring creation or extra arrays are required.

Time Complexity: O(n)
Space Complexity: O(1)
============================================================
"""

class Solution:
    def maxScore(self, s: str) -> int:
        count_left = 0
        count_right = 0

        for i in range(len(s)):
            if s[i] == '1':
                count_right += 1

        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                count_left += 1
            else:
                count_right -= 1

            score = count_left + count_right
            max_score = max(max_score, score)

        return max_score