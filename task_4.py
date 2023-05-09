a = int(input('Введите минимальное значение: '))
b = int(input('Введите максимальное значение: '))
x = int(input('Введите число: '))

def cah(a,b,x):
    y = x**2
    if a<y and y<b:
        print(y)
    else:
        print('Такого значения не существует')
    return a,b,x,y 

t = cah(a,b,x)
print(t)