from scipy import optimize
from service.function import *
from random import uniform

x = [uniform(-1,1), uniform(-1,1), uniform(-1,1)]
for error in eps:
    print("max error =", error)
    print(optimize.fmin(function, x, ftol=error, disp=1), "\n")
