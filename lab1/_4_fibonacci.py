from service.myfunction import *

class Fibonacci():
    array = [0, 1]
    n = 1
    def OneMore(self):
        """
        appends one more fibonacci number in array
        """
        self.array.append(self.array[self.n] + self.array[self.n - 1])
        self.n += 1
    def until(self, number):
        """
        calculates Fibonacci numbers until "number"
        """
        while (self.n + 1 < number):
            self.OneMore()
    def count_n(self):
        """
        counts how much fibonacci numbers is needed to calculate function with proper error
        error from myfunction
        """
        length = b - a
        while (error < length / 2):
            length = (b - a) / self.array[self.n]
            self.OneMore()
        return self.n + 1


fib = Fibonacci()
fib.count_n()
#print(f"Для вычисления с заданной точностью необходимо { fib.count_n() } чисел Фибоначчи")
required_steps = 0
x0 = 0
fx0 = 0
x1 = a + (b - a) * (fib.array[fib.n - 2] / fib.array[fib.n])
x2 = a + (b - a) * (fib.array[fib.n - 1] / fib.array[fib.n])
fx1 = function(x1)
fx2 = function(x2)
required_steps += 2
for i in range(fib.n - 1):
    if (fx1 <= fx2):
        b = x2
        x2 = x1
        fx2 = fx1
        x1 = a + b - x2
        fx1 = function(x1)
        required_steps += 1
    else:
        a = x1
        x1 = x2
        fx1 = fx2
        x2 = a + b - x1
        fx2 = function(x2)
        required_steps += 1
if (fx1 < fx2):
    x0 = x1
    fx0 = fx1
else:
    x0 = x2
    fx0 = fx2

print("Метод Фибоначчи")
print(f"x точки минимума: { x0 }")
print(f"Значение функции в точке минимума: { function(x0) }")
print(f'Количество обращений к функции: {required_steps}\n')