from fizical_constant import g 

m = 5
h = 10
V = 2

def mehanic(m=1, V=1, h=1):
    E = (m*V**2)/2 + m*g*h
    print(E)
    return E

print(mehanic(5,2,10))