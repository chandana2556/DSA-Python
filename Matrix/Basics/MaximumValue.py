
#maximum value in a matrix

m = [[1,2,3,4],
     [5,6,7,8],
     [9,0,1,2]]
rows = len(m)
cols = len(m[0])
maxv=0
for i in range(rows):
    for j in range(cols):
        if m[i][j]>maxv:
            maxv=m[i][j]
print("Maximum value : ",maxv)

Output:-

Maximum value :  9