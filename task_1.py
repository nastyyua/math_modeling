from random import random
import numpy as np

N=7  #или любое другое значение

def reshenie(a):
    s = 0
    for i in range(0,N,1):
        s += a[i]
    return s/N


b = np.zeros(N)
for i in range(0,N,1):
    b[i] = int(random()*100) 

x = reshenie(b)
print(b)
print(x) 