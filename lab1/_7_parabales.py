from service.myfunction import *
from random import uniform

x1 = a
x2 = b
x0 = (a+b)/2
c = uniform(a, b)
fx1 = function(x1)
fx2 = function(x2)
fxc = function(c)
required_steps = 3

while (True):
    t = c + 0.5 * (((x2-c)**2 * (fx1-fxc) - (c-x1)**2 * (fx2-fxc))/((x2-c) * (fx1-fxc) + (c-x1) * (fx2-fxc)))
    if (t != c):
        x0 = t
    else:
        x0 = (a+c)/2
    fx0 = function(x0)
    required_steps += 1

    if (x0 < c):
        if (fx0 < fxc):
            x2 = c
            c = x0
            fx2 = fxc
            fxc = fx0
        elif (fx0 > fxc):
            x1 = c
            fxa = fx0
        else:
            fx0 = fxc
            x1 = x0
            x2 = c
            c = (x0 + c) / 2
            fx1 = fx0
            fx2 = fxc
            fxc = function(c)
            required_steps += 1
    elif (x0 > c):
        if (fx0 < fxc):
            a = c
            c = x0
            fx1 = fxc
            fxc = fx0
        elif (fx0 > fxc):
            x2 = x0
            fx2 = fx0
        else:
            fx0 = fxc
            x1 = c
            x2 = x0
            c = (x0 + c) / 2
            fx1 = fxc
            fx2 = fx0
            fxc = function(c)
            required_steps += 1
    if ((x2 - x1) <= error):
        break

print("Метод парабол")
print(f"x точки минимума: { x0 }")
print(f"Значение функции в точке минимума: { function(x0) }")
print(f'Количество обращений к функции: {required_steps}\n')