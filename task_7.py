import numpy as np

a = []

x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))
x4 = int(input('Введите четвёртое число: '))

a.append(x1)
a.append(x2)
a.append(x3)
a.append(x4)
print(a)


c = int(input('Введите еще одно число: '))
m = int(input('Введите место в строке: '))

a = a[0:m-1] + [c] + a[m-1::1]

print(a) 