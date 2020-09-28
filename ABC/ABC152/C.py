n = int(input())
p = list(map(int, input().split()))
ans = 0
mn = float('inf')
for i in range(n):
    mn = min(p[i], mn)
    if mn == p[i]:
        ans += 1
print(ans)