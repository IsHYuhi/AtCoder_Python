from collections import Counter
from collections import deque
n, k = map(int, input().split())
a = Counter(list(map(int, input().split())))
a = [tuple(i) for i in a.items()]
a.sort(key=lambda x: x[1])
a = deque(a)
ans = 0
while k<len(a):
    ans += a.popleft()[1]
print(ans)