from collections import deque
n, m = map(int ,input().split())
a = list(map(int, input().split()))
if m == 0:
    print(1)
    exit()

a = deque(sorted(a))
va = []
s = 0
f = n
a.append(n+1)
m += 1
mi = n
for i in range(m):
    if a[i]-s-1>0:
        va.append(a[i]-s-1)
        mi = min(a[i]-s-1, mi)
    s = a[i]

if not va:
    print(0)
    exit()

#print(va)
#mi = min(va)
ans = 0

for j in va:
    r = 1 if j%mi > 0 else 0
    ans += j//mi+r
print(ans)