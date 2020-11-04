from collections import deque
import math

n, h = map(int, input().split())
ab = []
max_a = 0

for _ in range(n):
    a, b = map(int, input().split())
    max_a = max(max_a, a)
    ab.append([a, b])

ab.sort(key=lambda x: x[1], reverse=True)

bs = []
for i in range(n):
    if ab[i][1]>max_a:
        bs.append(ab[i][1])

ans = 0
bs = deque(bs)
while h>0 and bs:
    d = bs.popleft()
    h = h-d
    ans += 1

if h>0:
    ans += math.ceil(h/max_a)

print(ans)
