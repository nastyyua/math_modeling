from fizical_konstant import g
import numpy as np

V = 5
x1 = 1
y1 = 1

for t in range (0, 6, 1):
    x = x1 + V*t
    y = y1 + V*t - g*t**2/2
    a = np.zeros((1,3))
    a[0] = t 
    a[1] = x
    a[2] = y
    print(a)