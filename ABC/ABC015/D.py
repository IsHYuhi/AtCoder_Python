# w = int(input())
# n, k = map(int, input().split())
# a = []
# b = []
# for i in range(n):
#     a_, b_ = map(int,input().split())
#     a.append(a_)
#     b.append(b_)

# dp = [[0]*(w+1) for _ in range(n+1)]

# rest = w

# for i in range(n):
#     for j in range(w+1):
#         if a[i] > j:
#             dp[i+1][j] = dp[i][j]
#         else:
#             dp[i+1][j] = max(dp[i][j], dp[i][j-a[i]]+b[i])
# print(dp[n][w])







#3次元dp MLE

# w = int(input())
# n, k = map(int, input().split())
# a = []
# b = []
# for i in range(n):
#     a_, b_ = map(int, input().split())
#     a.append(a_)
#     b.append(b_)

# dp = [[[0] * (w + 1) for i in range(k + 1)] for j in range(n + 1)]

# # dp[i][j][l] := i 番目まで見て、j 枚使用し、幅が合計 l のときの最大値
# for i in range(n):
#     for j in range(k + 1):
#         for l in range(w + 1):
#             if j == k:  # この枚数以上貼れない
#                 dp[i + 1][j][l] = dp[i][j][l]
#             else:
#                 if l < a[i]:  # 幅が足りない
#                     dp[i + 1][j][l] = dp[i][j][l]
#                 else:
#                     dp[i + 1][j][l] = max(dp[i][j][l], dp[i][j - 1][l - a[i]] + b[i])

# # 必ず k 枚使う必要はない
# ans = 0
# for i in range(k + 1):
#     ans = max(ans, dp[n][i][w])

# print(ans)

w = int(input())
n, k = map(int, input().split())

dp = [[0] * (w + 1) for i in range(k + 1)]
ans=0
for i in range(n):
    a, b = map(int, input().split())
    for j in range(k, 0, -1):
        for l in range(w, 0, -1):
            if 0 <= l-a:
                dp[j][l] = max(dp[j][l], dp[j - 1][l - a] + b)
                ans = max(dp[j][l], ans)

print(ans)

# w = int(input())
# n, k = map(int, input().split())
# dp = [[0]*(w+1) for i in range(k+1)]
# ans = 0
# for _ in range(n):
#     a,b = map(int, input().split())
#     for j in range(k, 0, -1):
#         for p in range(w, 0, -1):
#             if p-a >= 0:
#                 dp[j][p] =max(dp[j][p], dp[j-1][p-a] + b)
#                 ans = max(ans, dp[j][p])

# print(ans)