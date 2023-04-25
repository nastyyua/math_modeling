import numpy as np

b = np.zeros((4,3))

for i in range(0, 4, 1):
    a = np.zeros((4,3))
    x1 = int(input('Введите первое значение: '))
    x2 = int(input('Введите второе значение: '))
    a[i][0] = x1
    a[i][1] = x2
    if x1>x2:
        a[i][2] = x1
    else:
        a[i][2] = x2
    b[i] = a[i]
    print(b)




