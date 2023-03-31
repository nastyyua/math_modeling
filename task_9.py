x = int(input('Введите число: '))
f = 0

while x>0:
    a = x%10
    x = x//10
    f = f*10 + a
print(f)