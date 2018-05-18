import numpy as np
#a = np.array([[0,1,0,0,0,1],[1,0,1,0,1,1]])
a = [[0,1,0,0,0,1],[1,0,1,0,1,1]]
def doit(a):
    return ''.join(map(str,a))

for r in range(0,2):
    print(doit(a[r]))
