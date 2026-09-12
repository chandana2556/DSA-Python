# LeetCode 1209 - Remove All Adjacent Duplicates in String II

## Description

Given a string `s` and an integer `k`, whenever **`k` same consecutive characters** appear, remove all those `k` characters.

We use a **stack** where each element stores:

* the character
* its current consecutive count

If the count reaches `k`, we remove that group using `pop()`.

### Approach: Stack with Character Count

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []

        for i in s:
            if st and st[-1][0] == i:
                st[-1][1] += 1

                if st[-1][1] == k:
                    st.pop()

            else:
                st.append([i, 1])

        ans = ""

        for ch, count in st:
            ans += ch * count

        return ans
```

### Time Complexity

**O(n)**

Each character is processed once, and stack operations take O(1).

> The final string construction is also linear overall.

### Space Complexity

**O(n)**

The stack can contain up to `n` character-count pairs.

## Example

**Input:**

```text
s = "deeedbbcccbdaa"
k = 3
```

**Process:**

```text
deeedbbcccbdaa
   eee → remove
      bbb → remove
        ccc → remove
```

After repeated removals:

```text
aa
```

**Output:**

```text
"aa"
```
