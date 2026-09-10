#Maximum in each row in a matrix

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,1,2]]
rows=len(m)
cols=len(m[0])
for i in range(rows):
    maxv=0
    for j in range(cols):
        if m[i][j]>maxv:
            maxv=m[i][j]
    print(maxv)

Output:-
4
8
10

#Minimum in each row in a matrix

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,1,2]]
rows=len(m)
cols=len(m[0])
for i in range(rows):
    minv=float("inf")
    for j in range(cols):
        if m[i][j]<minv:
            minv=m[i][j]
    print(minv)

Output:-
1
5
1
