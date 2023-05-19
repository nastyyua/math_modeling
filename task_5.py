from fizical_constant import pi
y = int(input('Если хотите найти площадь круга, введите 1, площадь треугольника - 2, площадь прямоугольника - 3: '))

def square(y):
    if y == 1:
        r = int(input('Радиус: '))
        s1 = pi*r**2
        print(s1)
    elif y == 2:
        a = int(input('Сторона: '))
        h = int(input('Высота: '))
        s2 = (a*h)/2
        print(s2)
    else:
        k = int(input('Первая сторона: '))
        f = int(input('Вторая сторона: '))
        s3 = k*f
        print(s3)

print(square(y)) 