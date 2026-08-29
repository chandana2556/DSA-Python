/*
============================================================
Problem: LeetCode 2351 - First Letter to Appear Twice
============================================================

Description:
Given a string s consisting of lowercase English letters,
return the first character that appears twice.

The answer is guaranteed to exist.

Example:
Input:
s = "abccbaacz"

Output:
"c"

The first character that appears for the second time is 'c'.


Edge Cases:
- Repeated character appears at the beginning
- Repeated character appears near the end
- Same character appears many times
- String contains only one distinct repeated character
*/


/*
============================================================
Approach 1: Dictionary / HashMap
============================================================

Use a dictionary to keep track of characters that have
already appeared.

For every character:
    If it is not present in the dictionary,
        add it.

    If it is already present,
        return that character.

Because we scan from left to right, the first character
we find again is the required answer.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def repeatedCharacter(self, s: str) -> str:

        d = {}

        for ch in s:

            if ch not in d:
                d[ch] = 1

            else:
                return ch


/*
============================================================
Approach 2: Set
============================================================

A set is designed to store unique elements.

For every character:
    If the character is already in the set,
        it is repeated, so return it.

    Otherwise, add it to the set.

We only need to know whether a character has appeared
before, so a Set is more appropriate than a Dictionary.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution:
    def repeatedCharacter(self, s: str) -> str:

        seen = set()

        for ch in s:

            if ch in seen:
                return ch

            seen.add(ch)


/*
============================================================
Approach 3: Frequency Array
============================================================

The string contains only lowercase English letters.

There are only 26 possible characters:
'a' to 'z'

So instead of using a HashSet or Dictionary, we can use
a fixed-size array of size 26.

Convert a character to an index using:

ch - 'a'

In Python:

ord(ch) - ord('a')

If the frequency is already greater than 0,
the character has appeared before.

Otherwise, mark it as seen.

Time Complexity: O(n)
Space Complexity: O(1)

The space is O(1) because the array always contains
only 26 positions.
*/

class Solution:
    def repeatedCharacter(self, s: str) -> str:

        freq = [0] * 26

        for ch in s:

            index = ord(ch) - ord('a')

            if freq[index] > 0:
                return ch

            freq[index] += 1


/*
============================================================
Approach 4: Boolean Array
============================================================

Since we only need to know whether a character has appeared
before, we don't actually need to store its complete
frequency.

A boolean array is enough.

True  → character has already appeared
False → character has not appeared yet

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution:
    def repeatedCharacter(self, s: str) -> str:

        seen = [False] * 26

        for ch in s:

            index = ord(ch) - ord('a')

            if seen[index]:
                return ch

            seen[index] = True


/*
============================================================
Approach Comparison
============================================================

Best choice:
Boolean Array / Frequency Array

Why?

The input contains only lowercase English letters,
so there are only 26 possible characters.

Therefore, a fixed array of size 26 gives constant
extra space.

Simplest approach:
Set 

Most optimized for the given constraints:
Boolean Array 
*/