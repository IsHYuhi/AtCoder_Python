n, k = map(int, input().split())
s = []
for i in range(k):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        s.append(j)
print(s)

coins = s
total = n-1
def combinations(coins, total):
    dp = [int(i % coins[0] == 0) for i in range(total + 1)]
    for coin in coins[1:]:
        count = 0
        for i in range(coin, total + 1):
            dp[i] += dp[i - coin]
            count += 1
    return dp[-1]
print(combinations(s, total))

# #dp =[[int(i % coins[0] == 0) for i in range(total + 1)] for j in range(total+1)]
# dp = [[0 for i in range(total + 1)] for j in range(total+1)]
# for j in range(total+1):
#     if dp[0][j] == 0:
#         dp[0][j] = 1
#         break

# for coin in coins:
#         for i in range(coin, total + 1):
#             for j in range(coin, total + 1):
#                 dp[j][i] += dp[j - coin][i - coin]
# print(dp[-1][-1]%998244353)