from itertools import combinations
n = int(input())
l = list(map(int, input().split()))
idx = [i for i in range(n)]
idx = combinations(idx, 3)
ans = 0
l.sort()
for i, j, k in idx:
    if l[i]!=l[j] and l[j]!=l[k] and l[k]!=l[i] and l[i]+l[j] > l[k]:
        ans += 1
print(ans)