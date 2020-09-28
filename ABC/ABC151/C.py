import numpy as np

n, m = map(int, input().split())
P = []
S = []
for i in range(m):
    p, s = input().split()
    P.append(int(p))
    S.append(s)

flag = [0 for i in range(n)]
wa =  [0 for i in range(n)]
for i in range(m):
    if S[i] == 'AC':
        flag[P[i]-1] = 1
    elif flag[P[i]-1] != 1:
        wa[P[i]-1] +=1

wa = sum(np.array(flag)*np.array(wa))
print(sum(flag), wa)
