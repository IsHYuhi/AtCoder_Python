n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
dp = [0]*(a[-1]+1)

for i in a:
    for j in range(i, max(a)+1, i):
        dp[j] += 1

for i in a:
    if dp[i]==1:
        ans += 1
print(ans)
