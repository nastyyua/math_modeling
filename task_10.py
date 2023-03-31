a = int(input('Введите натуральное число: '))

for i in range(1,a):
    while a%i==0 and i!=1 :
        b = a/i
        a = b
        print(i)