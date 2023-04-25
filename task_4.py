import numpy as np
N = 3
M = 5
msv = []

for i in range(N):
    a = []
    for j in range (M):
        a.append(np.sin(N*(i+1)+M*(j+1)))
    msv.append(a)

for i in range (N):
    for j in range(M):
        if msv[i][j] < 0:
            msv[i][j] = 0
        print (msv)
    else:
        print (msv)
    print()
