#sum of each row

m=[[1,2,3,4],[5,6,7,8],[9,0,1,2]]
rows=len(m)
cols=len(m[0])
for i in range(rows):
    total=0
    for j in range(cols):
        total=total+m[i][j]
        print(m[i][j],end=" ")
    #print()
    print("--> ",total)

Output:-
1 2 3 4 -->  10
5 6 7 8 -->  26
9 0 1 2 -->  12

#sum of each column

m = [[1,2,3,4],
     [5,6,7,8],
     [9,0,1,2]]

rows = len(m)
cols = len(m[0])

for i in range(cols):
    total = 0

    for j in range(rows):
        print(m[j][i], end=" ")
        total = total + m[j][i]

    print("--> ", total)

Output:-
1 5 9 --> 15
2 6 0 --> 8
3 7 1 --> 11
4 8 2 --> 14
