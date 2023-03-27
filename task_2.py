a = int(input('Введите первый член прогрессии:'))
b = int(input('Введите количество членов: '))
c = int(input('Введите знаменатель прогрессии: '))

i = range(a, c**(b-1)*a + 1, 1)
f = int(i[0])
print(f)

for i in range (1,b):
    x = a*c
    print(x)
    a=x
