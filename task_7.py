import numpy as np

n = int(input('Введите число: '))


def fin(n):
    s = np.zeros(n)   
    for i in range(2,1,n+1):
        s[0] = 0
        s[1] = 1
        s[i] = s[i-1] + s[i-2]
    print(s)

print(fin(5)) 


