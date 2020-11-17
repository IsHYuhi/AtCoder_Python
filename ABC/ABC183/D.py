import numpy as np

n, w = map(int, input().split())
stp = []
max_t = 0
for i in range(n):
    s, t, p = map(int, input().split())
    stp.append([s, t, p])
    max_t = max(t, max_t)

ans = np.array([0]*(max_t+1))

for s, t, p in stp:
    ans[s] += p
    ans[t] -= p

for i in range(1, max_t+1):
    ans[i] += ans[i-1]

for j in ans:
    if j>w:
        print('No')
        exit()
print('Yes')
