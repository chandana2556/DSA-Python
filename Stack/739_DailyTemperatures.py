# LeetCode 739 - Daily Temperatures

## Description

Given an array `temperatures`, for each day, find how many days you have to wait until a **warmer temperature**.

* If a warmer temperature exists, store the number of days to wait.
* If no warmer temperature exists, store `0`.

---

## Approach 1: Brute Force

For every temperature, check all the following days until we find a warmer temperature.

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    ans.append(j - i)
                    break
            else:
                ans.append(0)

        return ans
```

### Time Complexity

**O(n²)**

For each day, we may check all the remaining days.

### Space Complexity

**O(n)**

The `ans` array stores the result.

---

## Approach 2: Monotonic Stack

We use a stack to store the **indices of days whose warmer temperature has not been found yet**.

When the current temperature is greater than the temperature at the index on top of the stack:

* Pop that index.
* Calculate the number of days waited: `i - pos`.
* Store it in `r[pos]`.

The stack maintains temperatures in **decreasing order**.

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        r = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                pos = st.pop()
                r[pos] = i - pos

            st.append(i)

        return r
```

### Time Complexity

**O(n)**

Each index is pushed into the stack once and popped at most once.

### Space Complexity

**O(n)**

The stack and result array can store up to `n` elements.

### Best Approach

**Approach 2 - Monotonic Stack** is the optimal approach because it reduces the time complexity from **O(n²) to O(n)**.
