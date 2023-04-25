from fizical_konstant import g
import numpy as np

V = 5
x1 = 1
y1 = 1

for t in range (0, 6, 1):
    x = x1 + V*t
    y = y1 + V*t - g*t**2/2
    a = []
    a.append(t)
    a.append(y)
    a.append(x)
    print(a)