# Program to print a matrix by taking Rows and Columns line by line from the user 

#Take the no.of rows and columns from the user
rows=int(input("Enter no.of Rows: "))
cols=int(input("Enter no.of Columns: "))

#Empty List to store the matrix
m=[]

#Loop through each row 
for i in range(rows):

    #Create an empty list to store elements of the current row
    z=[]

    #Loop through each column
    for j in range(cols):

        #Take an integer input from the user
        a=int(input())

        # Add the entered element to the current row
        z.append(a)

    # Add the completed row to the matrix
    m.append(z)

# Print the complete matrix
print(m)

Output:-

Enter no.of Rows: 2
Enter no.of Columns: 3
1
2
3
4
5
6
[[1, 2, 3], [4, 5, 6]]


