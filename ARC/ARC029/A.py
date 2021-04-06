from itertools import combinations
n = int(input())
t = [int(input()) for _ in range(n)]
total = sum(t)

combs = []
for i in range(1, n+1):
    combs.extend(list(combinations(t, i)))

m = total
for c in combs:
    m = min(m, max(sum(c), total-sum(c)))
print(m)