n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = float('inf')

for i in range(n-k+1):
    if x[i] * x[i+k-1] < 0:
        ans = min(ans, abs(x[i])+abs(x[i+k-1])+min(abs(x[i]), abs(x[i+k-1])))
    else:
        ans = min(ans, max(abs(x[i]), abs(x[i+k-1])))

print(ans)
