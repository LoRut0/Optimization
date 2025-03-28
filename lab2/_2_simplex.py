from scipy import optimize
from service.function import *
from random import uniform

print(optimize.fmin(function, uniform(-1, 1)))
