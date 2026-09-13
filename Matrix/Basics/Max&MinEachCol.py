# Maximum in each column in a matrix
'''
m = [[1,2,3,4],
     [5,6,7,8],
     [9,0,1,2]]

rows = len(m)
cols = len(m[0])

for i in range(cols):
    maxv = 0

    for j in range(rows):
        if m[j][i] > maxv:
            maxv = m[j][i]

    print("Column", i + 1, "Maximum =", maxv)
'''

Output:-
Column 1 Maximum = 9
Column 2 Maximum = 6
Column 3 Maximum = 7
Column 4 Maximum = 8

# Minimum in each column in a matrix
m = [[1,2,3,4],
     [5,6,7,8],
     [9,0,1,2]]

rows = len(m)
cols = len(m[0])

for i in range(cols):
    minv = float("inf")

    for j in range(rows):
        if m[j][i] < minv:
            minv = m[j][i]

    print("Column", i + 1, "Minimum =", minv)

Output:-
Column 1 Minimum = 1
Column 2 Minimum = 0
Column 3 Minimum = 1
Column 4 Minimum = 2