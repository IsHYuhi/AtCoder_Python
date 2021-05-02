import numpy as np
from decimal import *
n, d, h = map(int, input().split())
ds = []
hs = []

h = Decimal(str(h))
d = Decimal(str(d))

for _ in range(n):
    d_, h_ = map(int, input().split())
    ds.append(Decimal(str(d_)))
    hs.append(Decimal(str(h_)))

ans = 1000
for i in range(-1, n):

    if i == -1:
        a = h/d
        b = 0
    else:
        a =  (h-hs[i])/(d-ds[i])# katamuki
        b = h-a*d

    flag = 0
    for j in range(n):
        if i==j:
            continue
        if a*ds[j]+b<hs[j]:
            flag = 1
            break

    if flag == 0:
        ans = min(ans, b)
print(max(ans, 0))