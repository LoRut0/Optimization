import math
def function (x):
    return -4 * x + math.e**(abs(x - 0.2))
def derivative(x):
    return ((5*x-1) * math.e ** (abs(5*x-1)/5))/(abs(5*x-1))-4
a = 0
b = 2
error = 1.5 * 10**-3