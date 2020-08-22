import math
from itertools import combinations
n, d = map(int, input().split())

def is_distance_int(y, z):
    ans = 0
    for i, j in zip(y, z):
        ans += (i-j)**2
    for k in range(1, ans+1):
        if k**2 == ans:
            return 1
    return 0

x = []
for i in range(n):
    x.append(list(map(int, input().split())))

c = [i for i in range(n)]
c = combinations(c, 2)

ans = 0
for i, j in c:
    ans += is_distance_int(x[i], x[j])

print(ans)