import numpy as np
s = np.zeros(5)
i = 3
s[0] = 0
s[1] = 1
s[i] = s[i-1] + s[i-2]
print(s[i])