n, x = map(int, input().split())
vp = [list(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    v, p = vp[i]
    total += v*p
    if total>x*100:
        print(i+1)
        exit()
print(-1)
