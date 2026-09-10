#Minimum value in a matrix

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,1,2]]
rows = len(m)
cols = len(m[0])
minv=float('inf')
for i in range(rows):
    for j in range(cols):
        if m[i][j]<minv:
            minv=m[i][j]
print("Minimum value : ",minv)

Output:-

Minimum value :  1
