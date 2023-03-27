a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a%b == 0:
    print(f'{a} делится на {b}')
    print(a/b, '- частное')
else:
    print(f'{a} не делится на {b}')
    print(a//b, '- частное')
    print(a%b, '- остаток')