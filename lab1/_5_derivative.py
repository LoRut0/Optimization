from service.myfunction import *

required_steps = 0
while (True):
    x0 = (a + b) / 2
    der_x0 = derivative(x0)
    required_steps += 1
    if (abs(der_x0) <= error):
        break
    if (der_x0 < 0):
        a = x0
    else:
        b = x0

print("Метод Больцано (производная)")
print(f"x точки минимума: { x0 }")
print(f"Значение функции в точке минимума: { function(x0) }")
print(f'Количество обращений к функции: {required_steps}\n')