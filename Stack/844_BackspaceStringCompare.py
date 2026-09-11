# LeetCode 844 - Backspace String Compare

## Description

Given two strings `s` and `t`, where `#` represents a **backspace**, compare the strings after applying all backspaces.

* If `#` appears, remove the previous character if one exists.
* Return `True` if both processed strings are equal; otherwise return `False`.

### Approach: Stack

We use two stacks, one for each string.

* If the character is not `#`, add it to the stack.
* If the character is `#`, remove the last character using `pop()` if the stack is not empty.
* Finally, compare both stacks.

### Code

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []

        for i in s:
            if i == '#':
                if st1:
                    st1.pop()
            else:
                st1.append(i)

        for i in t:
            if i == '#':
                if st2:
                    st2.pop()
            else:
                st2.append(i)

        return st1 == st2
```

### Time Complexity

**O(n + m)**

We traverse both strings once.

### Space Complexity

**O(n + m)**

The stacks may store characters from both strings.

## Example

**Input:**

```text
s = "ab#c"
t = "ad#c"
```

After applying backspaces:

```text
s = "ac"
t = "ac"
```

**Output:**

```text
True
```
