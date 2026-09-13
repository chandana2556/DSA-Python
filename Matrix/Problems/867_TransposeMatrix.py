# LeetCode 867 - Transpose Matrix

## Description

Given a matrix with `rows × cols` dimensions, return its **transpose**.

In the transpose:

* Rows become columns.
* Columns become rows.
* The element at `matrix[j][i]` becomes `mat[i][j]`.

We create a new matrix with `cols` rows and `rows` columns.

### Approach: Create a New Matrix

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        mat = []

        for i in range(cols):
            z = []

            for j in range(rows):
                z.append(matrix[j][i])

            mat.append(z)

        return mat
```

### Time Complexity

**O(rows × cols)**

Every element of the matrix is visited exactly once.

### Space Complexity

**O(rows × cols)**

We create a new matrix to store the transposed result.

## Example

**Input:**

```text
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

**Transpose:**

```text
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

**Output:**

```text
[[1, 4], [2, 5], [3, 6]]
```
