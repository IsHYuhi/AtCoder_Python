from collections import deque
import numpy as np

n, q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(q)]
ans = np.array([0]*(n+2))

for l, r in lr:
    ans[l] += 1
    ans[r+1] += 1
p = []
for i in range(1, n+1):
    ans[i] += ans[i-1]
    p.append(ans[i]%2)

print(''.join(map(str, p)))