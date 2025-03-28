from service.function import *
from service.golden_ratio import *
import numpy.linalg as linalg
from random import uniform

def diff(a, b):
    temp = a[::]
    for i in range(len(temp)):
        temp[i] -= b[i]
    return temp

def coordinate_descending(error):
    x = [uniform(-1,1), uniform(-1,1), uniform(-1,1)]
    x_prev = x[::]
    k = 0
    flag = False
    while (not flag):
        k += 1
        for i in range(3):
            x = golden_ratio(x, i, error)
            if (linalg.norm(diff(x, x_prev)) <= error):
                flag = True
                break
            else:
                x_prev = x[::]
    return x

for error in eps:
    print(coordinate_descending(error))