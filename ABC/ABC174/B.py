import math

n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for x, y in xy:
    if math.sqrt(x**2 + y**2)<=d:
        ans += 1
print(ans)
