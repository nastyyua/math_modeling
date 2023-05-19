import numpy as np

def simple_func(a, b, x):
    n = np.linspace(a, b, x)
    y = n ** 2
    print(y)


simple_func(-1, 1, 20)
