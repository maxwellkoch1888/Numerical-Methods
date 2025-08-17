import numpy as np
import matplotlib.pyplot as plt

g = 10
m = 10
c = 50

Vt = (g*m)/c
vt = Vt

# Part a) plot the mathematically derived eqn 2 where
# Vtx = velocity of the object
# vt = terminal velocity of the object
X = np.arange(0, 2, .01)
Vtx = vt*(1-np.exp((c/m)*-X))

# Part b) plot variation of velocity using eqn 3 where
# Vt = Velocity at following iteration
# vi = initial velocity
# t = time
# X = initial time
t = 0
timestep = .01
vi = 0
while t <= 2:
    t = t + timestep
    Vt = (vi + (g - (c/m)*vi)*timestep)
    vi = Vt
    plt.plot(t, Vt, 'o')

# Part e) using the program, find the time required to achieve 99.99% of terminal velocity
desired_percent = .9999
vn = vt*desired_percent
print("The velocity will be at 99.99% when time = ", np.interp(vn, Vtx, X, left = None, right = None), "seconds.")

# print graph of actual velocity and approximated velocity
plt.plot(X, Vtx, label = "Actual Velocity")
plt.legend()
plt.show()
