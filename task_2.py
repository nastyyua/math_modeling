import numpy as np
from numpy import tan 
from numpy import pi
from fizical_konstant import g

h = 100
a = np.pi / 3
b = 30

u = np.sqrt(g * h * np.tan(b)**2 / (2 * np.cos(a)**2 * (1-np.tan(b)*np.tan(a))))
print(u)

from fizical_konstant import ħ
from fizical_konstant import k
from fizical_konstant import e 

T = 200
ε = 300

N = 2 / np.sqrt(np.pi) * ħ / (k*T**(3/2)) * e**(-ε/k*T) * ε**(T/2)
print(N)
