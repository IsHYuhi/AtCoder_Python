n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ans = 0
for i, j in ab:
    ans += min(m, j)*i
    m -= min(m, j)
    if m == 0:
        print(ans)
        exit()
