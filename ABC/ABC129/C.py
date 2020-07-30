n, m = map(int, input().split())
am = [int(input()) for _ in range(m)]
hole = [False]*(n+1)

for i in am:
    hole[i] = True

dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    for j in range(i+1, min(n, i+2)+1):
        if not hole[j]:
            dp[j] += dp[i]
            dp[j] %=1000000007
print(dp[n])
