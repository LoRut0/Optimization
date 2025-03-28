import math
#-0.4223741099130859 x
#-0.4223741239218513 c


def f(x):
    return x ** 2 + 6 * math.exp(0.15 * x)


print(f(-0.4223741239218513))
print(f(-0.4223741099130859))
a = -1
b = 0
n = 22
c = (a + b) / 2
f1 = f(a)
f2 = f(b)
f3 = f(c)
for i in range(n):
    t = c + ((b - c) ** 2 * (f1 - f3) - (c - a) ** 2 * (f2 - f3)) / (2 * ((b - c) * (f1 - f3) + (c - a) * (f2 - f3)))
    if t == c:
        x = (a + c) / 2
    else:
        x = t
    f0 = f(x)
    if x < c:
        if f0 < f3:
            b = c
            c = x
            f2 = f3
            f3 = f0
        elif f0 > f3:
            a = x
            f1 = f0
        else:
            a = x
            b = c
            c = (x + c) / 2
            f1 = f0
            f2 = f3
            f3 = f(c)
    elif x > c:
        if f0 < f3:
            a = c
            c = x
            f1 = f3
            f3 = f0
        elif f0 > f3:
            b = x
            f2 = f0
        else:
            a = c
            b = x
            c = (x + c) / 2
            f1 = f3
            f2 = f0
            f3 = f(c)
        

print('x* =', x)
print('f(x*) =', f(x))
print('L =', b - a)