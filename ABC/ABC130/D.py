import numpy as np
import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))

cum = np.cumsum(a)

ans = 0
for i in range(n):
    if cum[i]>=k:
        ans += 1
        ans += bisect.bisect_right(cum, cum[i]-k)

print(ans)
