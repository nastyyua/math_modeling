from random import random
import numpy as np

N=7  #или любое другое значение

def reshenie(a):
    s = 0
    for i in range(0,N,1):
        s += a[0][i]
    return s/N


b = np.zeros((1,N))
for i in range(0,N,1):
    b[0][i] = int(random()*100) 

x = reshenie(b)
print(b)
print(x) 