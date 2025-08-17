import numpy as np

h = 1
g = 9.81
rho_air = 1.293
nu_air = 1.516e-5

def drag(Re):
    return (24/Re)+1.5

def rep(D, v):
    return D*v/nu_air

def mass(D):
    water = 1000 
    return np.pi/6*water*D**3

def equations(D, v0):
    t = 0
    x = 0
    y = 1.6 
    u = v0
    v = -.01
    A = np.pi*D**2/4
    CD = drag(rep(D, v))
    m = mass(D)

    while y > 0:
        dx = -0.5*CD*rho_air*A*u**2
        dy = -0.5*CD*rho_air*A*v**2

        ax = dx/m
        ay = (dy +(m-3.1415*rho_air*D**3)*g)/m

        un = u+ax*h
        vn = v+ay*h
        x = x+(un+u)*h/2
        y = y-(vn+v)*h/2
        t += h

    return x, t

Sizes = [16*10**(-6), 64*10**(-6), 128*10**(-6)]

Velocities = [1.5, 25, 50]

for D in Sizes:
    print("Aerosol size: %.0f μm" % (D*1e6))
    for v0 in Velocities:
        x, t = equations(D, v0)
        print("Velocity: %.1f m/s\tDistance: %.1f m\tTime taken: %.2f s" % (v0, x*10**-3,t))
