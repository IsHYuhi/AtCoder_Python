n = int(input())
h = list(map(int, input().split()))
ans = 1
mx = h[0]
for i in range(1, n):
    if h[i-1] <= h[i] and mx <= h[i]:
        ans += 1
    mx = max(mx, h[i])
print(ans)
