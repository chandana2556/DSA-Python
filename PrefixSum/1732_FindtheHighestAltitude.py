"""
============================================================
Problem: LeetCode 1732 - Find the Highest Altitude

Description:
A biker starts at altitude 0.

The gain[i] represents the net gain or loss in altitude
between two consecutive points.

For example:
    gain[i] = 5  -> altitude increases by 5
    gain[i] = -2 -> altitude decreases by 2

Find the highest altitude reached during the journey.

Concept:
This problem uses the Prefix Sum / Running Sum concept.

Instead of calculating the altitude from the beginning
again and again, we keep adding each gain to the current
altitude.

The maximum value of the running altitude is the answer.

Example:

Input:
gain = [-5, 1, 5, 0, -7]

Altitude:
0 -> -5 -> -4 -> 1 -> 1 -> -6

Highest Altitude = 1
============================================================
"""


"""
============================================================
Approach 1: Prefix Sum Array

- Create an array to store the altitude at every point.
- Start with altitude 0.
- For every gain, calculate the next altitude using:
      arr[i] = arr[i-1] + gain[i-1]
- Keep track of the maximum altitude.

Time Complexity: O(n)
Space Complexity: O(n)
============================================================
"""

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        arr = [0] * (len(gain) + 1)
        max_v = 0

        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] + gain[i - 1]
            max_v = max(max_v, arr[i])

        return max_v


"""
============================================================
Approach 2: Running Sum - Optimal

- We do not need to store every altitude.
- Maintain only the current altitude.
- Add each gain to altitude.
- Update max_altitude whenever a higher altitude is reached.

This is an optimized version of the prefix sum approach
because we only store the current altitude and maximum
altitude instead of the complete prefix sum array.

Time Complexity: O(n)
Space Complexity: O(1)
============================================================
"""

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        altitude = 0
        max_altitude = 0

        for i in range(len(gain)):
            altitude += gain[i]
            max_altitude = max(max_altitude, altitude)

        return max_altitude