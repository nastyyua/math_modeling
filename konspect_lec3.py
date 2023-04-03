a = 3 
b = 'Good'
c = ['Bad', 4, 'Molodec']

earth_mass =5.97237*10**30
sigma_steff_bolc = 5.67036713*10**(-8)
gravity_constant = 6.67408*10**(-11)

from konspect_lec3 import earth_mass as em
from konspect_lec3 import sigma_steff_bolc as G
from konspect_lec3 import gravity_constant as sigma

g = 500*G/10**2
print(g)

x = em*G*sigma
print(x)

import numpy as np
a = [1, 2, 4]
b = np.array(a)
print(type(a))
print(type(b))

print(b*b)
print(b/b)

print(b[-1])

a = np.zeros((2,3))
print(a)

a[0,2] = 5
print(a)

b = np.ones((3, 2))
print(b)

c = np.ndarray((3,3))
print(c)

print(type(a), type(b), type(c))

a = range(0, 5, 1)
print(a)

b = np.arange(0, 5, 0.1)
print(b)

d = np.linspace(0, 5, 10)
print(d)

a = [1,5,3,6]
slice = a[0:2:1]
print(slice)

slice = a[3:0:-1]
print(slice)

slice = a[::-1]
print(slice)

b = np.array([a, np.array(a)*3])
print(b)

slice = b[::, 1]
print(slice)

slice = b[1, 2:3:1]
print(slice)

slice =b[1, 2::1]
print(slice)