import math
import random

z = 10
m = 100
c = 5
v = 5
g = 9.81
t = .50329592
initial = 1

# part a- calculate the maximum height graphically
height = z + (m/c)*(v + (m*g)/c)*(1-math.e**((-1*c*t)/m)) - (m*g*t)/c
print("The maximum height is", height,".")
print("---------------")

# part b- calculate the height to an error of .01%
error = 1
while error >= .01:
    velocity =(v+(g*m)/c)*math.e**((-1*c*initial)/m)-(g*m)/c
    acceleration = -1*((c*v + g*m)*math.e**((-1*c*t)/m))/m
    f = initial - velocity/acceleration
    initial = f
    error = (initial - t)/t
    if error < 0:
        error = error*-1
Height = z + (m/c)*(v + (m*g)/c)*(1-math.e**((-1*c*f)/m)) - (m*g*f)/c
print("With Newton's Method")
print("Height: ", Height)
print("Time: ", f)
print("Error: ", error*100, "%")
print("---------------")

