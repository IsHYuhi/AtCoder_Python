n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
ans = float('inf')
for i in range(n-k+1):
    ans = min(h[i+k-1] - h[i], ans)
print(ans)