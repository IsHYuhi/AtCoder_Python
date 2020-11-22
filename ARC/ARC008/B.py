from collections import Counter
import math
n, m = map(int, input().split())
name = Counter(list(input()))
kit = Counter(list(input()))

ans = 0
for l, c in name.items():
    if c > kit[l]*n:
        print(-1)
        exit()
    else:
        ans = max(math.ceil(c/kit[l]), ans)
print(ans)

