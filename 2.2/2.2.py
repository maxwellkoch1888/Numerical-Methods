import numpy as np
m = []

# a = number of rows
# b = number of columns
a = int(input("How many rows are there? "))
b = int(input("How many columns are there? "))


# c = row counter
# y = column counter
c = 0
while c < a:
    line = []
    y = 0
    while y < b:
        line.append(float(input("List matrix values top to bottom, left to right. ")))
        y += 1
        if y == b:
            m.append(line)
    c += 1


# matrix = create a matrix from nested lists
# length = tells how many lists are in the matrix i.e. how many rows are there?
matrix = np.array(m)
length = len(matrix)
print("Original Matrix")
print(matrix)

# k = new row counter. i.e. What row are we looking at?
# i = new column counter. i.e. what column are we looking at?

def eliminate():
    for k in range(length-1):
        pivot()
        for i in range(k+1, length):
            factor = float(matrix[i, k] / matrix[k, k])
            difference = b-a
            for j in range(k, length+difference):
                o = matrix[i,j]
                d = factor*matrix[k,j]
                new = o-d
                matrix[i, j] = new


def pivot():
    # max = defines the maximum value of the column. Assumed to be the first row at the start of pivot().
    # row_max = placeholder for the row with the highest value in the current column. Assumed to be the first row at the start of pivot().
    for i in range(0,length):
        max = abs(matrix[i][i])
        row_max = i 
        
        # Find the row with the maximum absolute value.
        for k in range(i+1, length):
            if abs(matrix[k][i])> max:
                max = abs(matrix[k][i])
                row_max = k
                
        # Swap current row with row of maximum absolute value.
        for k in range(i, length):
            intermediate = matrix[row_max][k]
            matrix[row_max][k] = matrix[i][k]
            matrix[i][k] = intermediate

eliminate()
print("matrix after eliminate")
print(matrix)
