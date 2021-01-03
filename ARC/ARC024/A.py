from collections import Counter
l, r = map(int, input().split())
ls = Counter(list(map(int, input().split())))
rs = Counter(list(map(int, input().split())))

keys = set(ls.keys()) & set(rs.keys())

ans = 0
for key in keys:
    ans += min(ls[key], rs[key])

print(ans)