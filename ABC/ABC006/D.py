from bisect import bisect_left
n = int(input())
c = [int(input()) for _ in range(n)]

dp = [float('inf')] * n

for i in range(n):
    dp[bisect_left(dp, c[i])] = c[i]
print(n - bisect_left(dp, float('inf')))


'''O(n^2) TLE'''
# dp = [0]*(n+1)

# res = 0
# for i in range(n):
#     dp[i] = 1
#     for j in range(n):
#         if c[j] < c[i]:
#             dp[i] = max(dp[i], dp[j]+1)
#         res = max(dp[i], res)
# print(n-res)

