import math
import matplotlib.pyplot as plt
import numpy as np


# f = friction factor
# e = roughness in the pipe (mm)
# D = pipe diameter (m)
# R = reynold's number
f = .008
D = float(input("What is the pipe diameter (range 0.1-10m)? "))
R = 10**int(input("What is the order of the Reynold's number (range 4-6)? "))
E = .0015/D

# Part a, calculate friction factor for ranges of values
i = 0
while i < 10:
    fx = 1/(f**.5) + 2*math.log(E/(3.7) + 2.51/(R* (f**.5)), 10)
    first_derivative = -.5*(f**-1.5)*(1 + ((2.18261/R)*(E/(3.7) + 2.51/(R* (f**.5)))**-1))
    i += 1
    f = f - fx/first_derivative
print("The friction factor is ", f, ".")

# Part b, plot the colebrook equation and the swamee-jain approximation for varying values of d and Re
j = .00015
while j < .016:
    r = 10000
    x = []
    y = []
    while r in range(10**4, 10**6):
        fx = 1/(f**.5) + 2*math.log(j/(3.7) + 2.51/(r* (f**.5)), 10)
        first_derivative = -.5*(f**-1.5)*(1 + ((2.18261/r)*(j/(3.7) + 2.51/(r* (f**.5)))**-1))
        i += 1
        f = f - fx/first_derivative
        y.append(f)
        x.append(r)
        r +=100
    plt.plot(x,y, color = "black")
    j +=.0015

j = .00015
while j < .016:
    x = np.linspace(10000, 1000000, 100)
    swamee = 1.325/(np.log(j/(3.7) + 5.74/(x**.9)))**2
    plt.plot(x, swamee, '-', color = "red")
    j += .0015

plt.xscale('log')
plt.ylim(0.01,.05)
plt.xlabel("Reynold's Number")
plt.ylabel("Friction Factor")
plt.title("Friction factor with changing Re and D")
plt.show()

#Part c- calculate the pressure gradient for a pipe of d = 2m and roughness = .0015mm
v = 1
q = []
pl = []
while v < 10:
    p = 1
    mu = 0.00102
    Re = (p*v*2)/mu
    f = 1.325/(np.log((7.5*10**(-4))/(3.7) + 5.74/(Re**.9)))**2
    flow = v*math.pi
    pressure = (f*2*997*flow**2)/(8*(math.pi)**2)
    q.append(flow)
    pl.append(pressure)
    v += .1
    plt.plot(q,pl, color = "red")

plt.xlabel("Flow (Q)")
plt.ylabel("Pressure Gradient")
plt.title("Pressure Gradient with changing Flow")
plt.show()