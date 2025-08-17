import math
import random

# part c- find values of m and v for max altitude using random search method
maxfn = 0
i = 1
j = 1
initial = 1

while i < 1000000:
    M = 2500*random.random()
    V = (2500*2/M)**.5
    f = 10*random.random()
    fn = 10 + (M / 10) * (V + (M * 9.81) / 10) * (1 - math.e ** ((-1 * 10 * f) / M)) - (M * 9.81 * f) / 10
    if fn > maxfn:
        maxfn = fn
        maxM = M
        maxV = V
    i = i + 1
    # print("Max: ", fn)
    # print("m: ", M)
    # print("v: ", V)
print("Maximum value: ", maxfn)
print("Max value of m: ", maxM)
print("max value of v: ", maxV)
