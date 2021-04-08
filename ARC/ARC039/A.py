import numpy as np
a, b = map(list, input().split())
ans = - float('inf')

for i in range(3):
    au = a.copy()
    au[i] = '9'
    ans = max(int(''.join(au))-int(''.join(b)), ans)

for i in range(3):
    bl = b.copy()
    if i == 0:
        bl[i] = '1'
    else:
        bl[i] = '0'
    ans = max(int(''.join(a))-int(''.join(bl)), ans)

print(ans)
