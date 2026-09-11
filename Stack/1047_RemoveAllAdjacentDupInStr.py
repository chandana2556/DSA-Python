# LeetCode 1047 - Remove All Adjacent Duplicates In String

## Description

Given a string `s`, repeatedly remove **adjacent duplicate characters** until no adjacent duplicates remain.

We use a **stack**:

* If the stack is not empty and the current character is the same as the stack's top character, remove the top character using `pop()`.
* Otherwise, add the current character using `append()`.
* Finally, join the stack to get the answer.

### Approach: Stack

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []

        for i in s:
            if st and i == st[-1]:
                st.pop()
            else:
                st.append(i)

        return ''.join(st)
```

### Time Complexity

**O(n)**

We traverse the string once, and each character is pushed and popped at most once.

### Space Complexity

**O(n)**

The stack can contain up to `n` characters.

## Example

**Input:**

```text
s = "abbaca"
```

**Process:**

```text
abbaca
 ↓
aaca
 ↓
ca
```

**Output:**

```text
"ca"
```
