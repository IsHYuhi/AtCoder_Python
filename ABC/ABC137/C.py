from collections import Counter
n = int(input())
s = [tuple(sorted(input())) for _ in range(n)]

c = Counter(s)
ans = 0
for i in c.values():
    ans += i*(i-1)//2
print(ans)
