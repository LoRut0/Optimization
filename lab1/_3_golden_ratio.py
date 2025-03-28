from service.myfunction import *

length = b - a

required_steps = 0

alph = (5**0.5 - 1) / 2
x1 = a + ( 1 - alph ) * ( b - a )
x2 = a + alph * ( b - a )
fx1 = function(x1)
fx2 = function(x2)
required_steps += 2

while (True):
    if (fx1 < fx2):
        b = x2
        x2 = x1
        fx2 = fx1
        x1 = a + ( 1 - alph ) * ( b - a )
        fx1 = function(x1)
        required_steps += 1
    else:
        a = x1
        x1 = x2
        fx1 = fx2
        x2 = a + alph * ( b - a )
        fx2 = function(x2)
        required_steps += 1
    length = b - a
    delta = length / 2
    if (delta <  error):
        x0 = (b + a) / 2
        break
    
print("Метод золотого сечения")
print(f"x точки минимума: { x0 }")
print(f"Значение функции в точке минимума: { function(x0) }")
print(f'Количество обращений к функции: {required_steps}\n')