n, m = map(int, input().split())

d = [[float('inf')]*n for _ in range(n)]
for i in range(m):
    a, b, t = map(int, input().split())
    d[a-1][b-1] = t
    d[b-1][a-1] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

worst = float('inf')
for i in range(n):
    d[i][i] = 0
    worst = min(max(d[i]), worst)
print(worst)
