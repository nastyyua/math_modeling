a = int(input('Введите число: '))

for i in range(2,a):
    s = 0
    for f in range(1, int(i/2+1)):
        if i%f==0:
            s +=f
    if s==i:
        print(s)