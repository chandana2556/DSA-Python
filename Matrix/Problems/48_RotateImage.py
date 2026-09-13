# LeetCode 48 - Rotate Image

## Description

Given an `n × n` matrix, rotate the matrix **90 degrees clockwise**.

The matrix must be modified **in-place** and nothing should be returned.

There are three approaches:

1. Extra Matrix
2. Transpose + Reverse Rows
3. Reverse Columns + Transpose

---

## Approach 1: Extra Matrix

Create a new matrix and directly place each element at its rotated position.

For an element at `matrix[i][j]`, its new position is:

`result[j][n - 1 - i]`

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        mat = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                mat[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = mat[i][j]
```

### Time Complexity

**O(n²)**

Every element is visited.

### Space Complexity

**O(n²)**

A new matrix is created.

---

## Approach 2: Transpose + Reverse Rows

First, **transpose** the matrix:

* Convert rows into columns.
* Swap `matrix[i][j]` with `matrix[j][i]`.

Then **reverse every row**.

This results in a 90° clockwise rotation.


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for i in range(n):
            matrix[i].reverse()


### Time Complexity

**O(n²)**

### Space Complexity

**O(1)**

The rotation is performed completely in-place.

---

## Approach 3: Reverse Columns + Transpose

This is the approach you provided.

First, reverse every column:


Top ↔ Bottom


Then transpose the matrix.

After these two operations, the matrix is rotated 90° clockwise.


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # Reverse every column
        for i in range(cols):
            st = 0
            ed = rows - 1

            while st < ed:
                matrix[st][i], matrix[ed][i] = matrix[ed][i], matrix[st][i]
                st += 1
                ed -= 1

        # Transpose
        for i in range(rows):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### Time Complexity

**O(n²)**

Column reversal takes O(n²) and transpose takes O(n²).

### Space Complexity

**O(1)**

No extra matrix is created.

---

## Example

**Input:**


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

**After 90° clockwise rotation:**


[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]


**Output:**


[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]


### Best Approach

**Approach 2: Transpose + Reverse Rows** is generally the simplest and most commonly used optimal approach.

**Approach 3** is also optimal and is a good alternative way to understand matrix rotation.
