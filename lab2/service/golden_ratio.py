from .function import *

def golden_ratio(x, x_num, error):
    '''
    x - array of x\n
    x_num  - number of x, through which algo seeks\n
    error - max error, lenght/2 of final interval
    '''
    array_left = x[::]
    array_right = x[::]
    a = x[x_num] - 1
    b = x[x_num] + 1

    alph = (5**0.5 - 1) / 2
    x1 = a + ( 1 - alph ) * ( b - a )
    x2 = a + alph * ( b - a )
    array_left[x_num] = x1
    array_right[x_num] = x2
    fx1 = function(array_left)
    fx2 = function(array_right)

    while (True):
        if (fx1 < fx2):
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = a + ( 1 - alph ) * ( b - a )
            array_left[x_num] = x1
            fx1 = function(array_left)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + alph * ( b - a )
            array_right[x_num] = x2
            fx2 = function(array_right)
        delta = (b - a) / 2
        if (delta <  error):
            x[x_num] = (b + a) / 2
            break
    return x