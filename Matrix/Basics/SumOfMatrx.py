
#Sum of the matrix

m=[[1,2,3,4],[5,6,7,8],[9,0,1,2]]
rows=len(m)
cols=len(m[0])
total=0
for i in range(rows):
    for j in range(cols):
        total=total+m[i][j]
        print(m[i][j],end=" ")
    print()
print("Sum = ",total)

Output:- 
1 2 3 4 
5 6 7 8 
9 0 1 2 
Sum = 48
