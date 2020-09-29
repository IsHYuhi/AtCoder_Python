import math
a, b = map(int, input().split())
ans = float('inf')
for x in range(1001):
    if int(math.floor(x*1.08))-x==a and int(math.floor(x*1.1))-x==b:
        ans = min(ans, x)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
