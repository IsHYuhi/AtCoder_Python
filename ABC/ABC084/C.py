n = int(input())
c = []
s = []
f = []
for _ in range(n-1):
    _c, _s, _f = map(int, input().split())
    c.append(_c)
    s.append(_s)
    f.append(_f)

ans = 0

for i in range(n):
    ans = 0
    for j in range(i, n-1):
        if ans < s[j]:
            ans = s[j] + c[j]
        elif ans % f[j] == 0:
            ans += c[j]
        else:
            ans += f[j] - ans%f[j] + c[j]

    print(ans)
