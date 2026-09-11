# LeetCode 2390 - Removing Stars From a String

## Description

Given a string `s` containing lowercase English letters and `*`.

For every `*`, remove the **closest non-star character to its left**.

We use a **stack** to store the characters.

* If the character is `*`, remove the last character using `pop()`.
* Otherwise, add the character to the stack using `append()`.
* Finally, join the stack to form the resulting string.

### Approach: Stack

```python
class Solution:
    def removeStars(self, s: str) -> str:
        st = []

        for i in s:
            if i == '*':
                st.pop()
            else:
                st.append(i)

        return ''.join(st)
```

### Time Complexity

**O(n)**

We traverse the string once.

### Space Complexity

**O(n)**

The stack can store up to `n` characters.

## Example

**Input:**

```text
s = "leet**cod*e"
```

**Process:**

```text
leet**cod*e
    ↓
lee       (first two stars remove t and e)
       ↓
leecod    (star removes d)
```

**Output:**

```text
"lecoe"
```
