import numpy as np
K, N = map(int,input().split())
As = list(map(int, input().split()))
As = np.array(As)
Bs = np.copy(As)
As = np.append(As, 0)
Bs = np.append(0, Bs)
Cs = As-Bs
Cs = np.delete(Cs, 0, 0)
Cs = np.delete(Cs, -1, 0)
Cs = np.append(Cs, As[0]+K-As[-2])
idx = np.argmax(Cs)
print(K-Cs[idx])