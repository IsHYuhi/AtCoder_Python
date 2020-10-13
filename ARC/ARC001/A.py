from collections import Counter
n = int(input())
c = list(input())
c = Counter(list(map(int, c)))


mn = float('inf')
mx = -1

if len(c)!=4:
    mn = 0

for v in c.values():
    mn = min(v, mn)
    mx = max(v, mx)

print(mx, end=' ')
print(mn)
