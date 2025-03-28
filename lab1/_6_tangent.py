from service.myfunction import *

x1 = a
x2 = b
fx1 = function(x1)
fx2 = function(x2)
der_x1 = derivative(x1)
der_x2 = derivative(x2)
required_steps = 4
while (True):
    if (( x2 - x1 ) / 2 < error):
        x0 = (x1 + x2)/2
        break
    c = ((x2*der_x2 - x1*der_x1) - (fx2 - fx1))/(der_x2 - der_x1)
    fxc = function(c)
    der_c = derivative(c)
    required_steps += 2
    if (der_c == 0):
        x0 = c
        break
    elif (der_c < 0):
        x1 = c
        fx1 = fxc
        der_x1 = der_c
    else:
        x2 = c
        fx2 = fxc
        der_x2 = der_c

print("Метод касательной")
print(f"x точки минимума: { x0 }")
print(f"Значение функции в точке минимума: { function(x0) }")
print(f'Количество обращений к функции: {required_steps}\n')