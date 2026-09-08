Taking the input from user as a single row values at a time

# Take the number of rows from the user
rows = int(input("Enter no.of Rows: "))

# Take the number of columns from the user
cols = int(input("Enter no.of Columns: "))

# Create an empty list to store the complete matrix
m = []

# Loop runs 'rows' number of times to create each row
for i in range(rows):

    # Take one complete row as input
    # split() separates the input values by spaces
    # map(int, ...) converts each value from string to integer
    # list() converts the map object into a list
    z = list(map(int, input().split()))

    # Add the current row to the matrix
    m.append(z)

# Print the complete matrix
print(m)


Output:-
Enter no.of Rows: 2
Enter no.of Columns: 3
1 2 3
4 5 6
[[1, 2, 3], [4, 5, 6]]