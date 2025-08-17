import numpy as np
m = []
n = []

a = int(input("How many rows are there? "))
b = int(input("How many columns are there? "))
c = 0

while c < a:
    line = []
    y = 0
    while y < b:
        # line.append(randint(0,10))
        line.append(float(input("List matrix values top to bottom, left to right. ")))
        y += 1
        if y == b:
            m.append(line)
            n.append(line)
    c += 1
matrix = np.array(m)
original = np.array(n)
length = len(matrix)
print("Original Matrix")
print(matrix)
print()

def upper():
    def eliminate():
        for k in range(length-1):
            for i in range(k+1, length):
                factor = float(matrix[i, k] / matrix[k, k])
                difference = b-a
                for j in range(k, length+difference):
                    o = matrix[i,j]
                    d = factor*matrix[k,j]
                    new = round(o-d, 3)
                    matrix[i, j] = new
    eliminate()
    print(matrix)


def lower():
    mat = []
    c = 0
    while c < a:
        line = []
        y = 0
        while y < b:
            if y ==0:
                line.append(float(1))
            else:
                line. append(float(0))
            y += 1
            if y == b:
                mat.append(line)
        c += 1
    low = np.array(mat)

    def replace():
        for k in range(length - 1):
            for i in range(k+1, length):
                factor = float(original[i, k] / original[k, k])
                difference = b - a
                for j in range(k, length + difference):
                    o = original[i,j]
                    d = factor*original[k,j]
                    new = round(o-d, 3)
                    original[i, j] = new


                    if j < i:
                        low[i, j] = factor
                    elif j == i:
                        low[i,j] = 1
                    elif j > i or i == 0:
                        low[i,j] = 0 
    replace()
    print(low)
    
def substitute():
    Up = upper()
    Low = lower()
       
    I = []
    c = 0
    while c < a:
        i = []
        y = 0
        while y < b:
            if y == c:
                i.append(float(1))
            else:
                i.append(float(0))
            y += 1
            if y == b:
                I.append(i)
        c += 1
    identity = np.array(I)

    invert = []
    for iteration in range(a):
        vector = identity[:,iteration]
        sol = np.linalg.inv(Low).dot(vector)
        column = np.linalg.inv(Up).dot(sol)
        invert.append(column)
    inverse_transpose = np.array(invert)
    inverse = inverse_transpose.transpose()
    print("Matrix Inverse")
    print(inverse)

# substitute()
upper()
lower()