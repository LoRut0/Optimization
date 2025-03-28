from service.myfunction import *

length = b - a
required_steps = 0
x0 = ( b + a ) / 2

while (True):
    x1 = a + length / 4
    x2 = b - length / 4
    fx0 = function(x0)
    fx1 = function(x1)
    fx2 = function(x2)
    required_steps += 3
    if (fx1 < fx0):
        b = x0
        x0 = x1
    else:
        if (fx2 < fx0):
            a = x0
            x0 = x2
        else:
            a = x1
            b = x2
    length = b - a
    delta = length / 2
    if (delta <  error):
        x0 = (b + a) / 2
        break
    
print("Метод дихотомии")
print(f"x точки минимума: { x0 }")
print(f"Значение функции в точке минимума: { function(x0) }")
print(f'Количество обращений к функции: {required_steps}\n')
