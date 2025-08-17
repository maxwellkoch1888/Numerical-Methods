import math

# correction method
# yi = 1
# t = 0 
# 
# 
# while t < 2.5:
#     fx = yi * t ** 3 - 1.5 * yi
#     y0 = yi + fx * .5
#     print("initial y: ", yi)
#     print("initial t: ", t)
#     print("y0: ", y0)
#     print("fx: ", fx)
#     yn = yi + (fx*.5 + y0*(t+.5)**3-1.5*y0)*.5*.5
#     yi = yn
#     t = t + .5
#     print("new y: ", yn)
#     print("---------------")


# RK-4 method

# yi = 1
# ti = 0 
# h = .5
# 
# def function(ti,yi):
#     fx = yi*ti**3-1.5*yi
#     return fx
# 
# while ti< 2.5:
#     k1 = function(ti, yi)
#     k2 = function(ti+.25*h, yi+.25*k1*h)
#     k3 = function(ti+.25*h, yi-.125*k1*h+.125*k2*h)
#     k4 = function(ti+.5*h, yi-.5*k2*h+k3*h)
#     k5 = function(ti +.75*h, yi+.1875*k1*h+.5625*k4*h)
#     k6 = function(ti+h, yi-(3/7)*k1*h+(2/7)*k2*h+(12/7)*k4*h+(8/7)*k5*h)
#     
#     fx = yi + (7*k1+32*k3+12*k4+32*k5+7*k6)*h/90
#     yi = fx
#     ti = ti +.5
#     print("k1: ", k1)
#     print("k2: ", k2)
#     print("k3: ", k3)
#     print("k4: ", k4)
#     print("k5: ", k5)
#     print("k6: ", k6)
#     print("new y:" ,fx)
#     print("---------------")
#     
# Euler's method explicit
# yi = 0
# ti = 0
# h = .001
# 
# while ti < .006:
#     fx = -1000 * yi + 3000 - 2000 * math.exp(-ti)
#     yn = yi +fx*h
#     yi = yn 
#     print("time: ", ti)
#     print("New y: ", yi)
#     print("---------------")
#     ti = ti + .001

# Euler's method implicit
yi = 0
ti = 0
h = .05

while ti < .35:
    yn = (yi + 3000*h - 2000*h*math.exp(-1*(ti+h)))/(1 + 1000*h)
    print("time: ", ti)
    print("y: ", yi)
    print("---------------")
    yi = yn
    ti = ti + h