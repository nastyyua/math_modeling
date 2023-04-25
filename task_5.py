from task_4 import *

for i in range(N):
    for j in range(M):
        a = msv[i][0]
        msv[i][0] = msv [i][1]
        msv[i][1] = a 
        print(msv)
