from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = Counter(a+b)

ans = []
for k, v in c.items():
    if v == 1:
        ans.append(k)

ans.sort()
print(' '.join(map(str, ans)))
