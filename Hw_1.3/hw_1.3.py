from random import randint
import statistics as s

list1 = []
n = 0 

while n < 10:
    list1.append(randint(1, 100))
    n += 1

def sort():
    list1.sort()
    print("Numbers =",list1)

def mean():
    x = sum(list1)
    y = x/10
    print("Mean =", y)

def median():
    list1.sort()
    x1 = list1[4]
    x2 = list1[5]
    Median = (x1+x2)/2
    print("Median =", Median)

def mode():
    z = s.multimode(list1)
    if len(z) == 10:
        print("There is no mode.")
    else:
          print("Mode(s) =", z)

sort()
mean()
median()
mode()
