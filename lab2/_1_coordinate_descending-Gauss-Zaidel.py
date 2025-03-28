from service.function import *
from service.golden_ratio import *
import numpy.linalg as linalg
from random import uniform

def coordinate_descending(error):
    x = [uniform(-1,1), uniform(-1,1), uniform(-1,1)]
    k = 0
    flag = False
    while (not flag):
        k += 1
        for i in range(3):
            x = golden_ratio(x, i, error)
            if (linalg.norm(x) <= error):
                flag = True
                break
    return x

for error in eps:
    print(coordinate_descending(error))