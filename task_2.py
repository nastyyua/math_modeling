from fizical_konstant import g 
import math as mt
import numpy as np

h = 100
a = mt.pi/3
b = mt.pi/6

c = 1 - mt.tan(b)*mt.tan(a)
n = 2*mt.cos(b)**2
m = mt.tan(b)**2
z = g*h

print( c, n, m ,z)


