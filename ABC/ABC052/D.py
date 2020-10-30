n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if a*(x[i+1]-x[i])>=b:
        ans += b
    else:
        ans += a*(x[i+1]-x[i])

print(ans)