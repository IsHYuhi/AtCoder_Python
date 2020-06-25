import itertools
N, K= map(int,input().split())
p = list(map(int, input().split()))
p.sort()
ans = sum(p[:K])
# ans = 1000000
# def dfs(i, sum):
#     print(sum)
#     global ans
#     if i == N-1:
#         ans = min(ans, sum)
#         return
#     dfs(i+1, sum + p[i])
#     dfs(i+1, sum)

# dfs(0, 0)
# print(ans)
# ans = 1000000
# for i in itertools.combinations(p, K):
#     s = sum(i)
#     ans = min(ans, s)
print(ans)
