n, k = map(int, input().split())
k = abs(k)
ans = 0
for x in range(k+2, 2*n+1):
    ans += min(x-k-1, 2*n+1-x+k) * min(x-1, 2*n+1-x)
print(ans)