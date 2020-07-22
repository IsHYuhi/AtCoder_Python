from collections import Counter
n = int(input())
s = Counter([input() for _ in range(n)])

m = int(input())
t = Counter([input() for _ in range(m)])

keys = s.keys() & t.keys()
for key in keys:
    s[key] -= t[key]

print(max(max(s.values()), 0))
