h, w = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(h)]
mn = 100
for i in field:
    mn = min(mn, min(i))

ans = 0
for i in range(h):
    for j in range(w):
        ans += abs(field[i][j]-mn)

print(ans)