from service.myfunction import *

required_steps = math.ceil((b-a)/error)
step = ((b-a)/required_steps)
list_of_xy = {}
x = 0
for i in range(required_steps):
    list_of_xy.update({ x : function(x) })
    x+=step
min_y = min(list_of_xy.values())
min_x = [key for key, val in list_of_xy.items() if val == min_y]

print("Метод перебора на равномерной сетке")
print(f'x минимума функции: { min_x[0] }') 
print(f"Значение функции в точке минимума: { min_y }")
print(f'Количество обращений к функции: {required_steps}\n')
