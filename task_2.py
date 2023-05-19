from random import random
import numpy as np

N=5

def reshenie(a):
    s = 1
    for i in range(0,N,1):
        s *= a[i]
    return s


b = np.zeros(N)
for i in range(0,N,1):
    b[i] = int(random()*100) 

x = reshenie(b)
print(b)
print(x) 