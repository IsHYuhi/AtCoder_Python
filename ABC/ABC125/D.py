n = int(input())
a = list(map(int, input().split()))

under = len([i for i in a if i<0])
zero = False
if 0 in a:
    zero = True

a = list(map(abs, a))
a.sort()
if under%2==0 or zero:
    print(sum(a))
else:
    print(sum(a)-2*a[0])

'''AC with DP'''
'''
dp = [[0]*(n+1) for i in range(2)]
dp[0][0] = 0
dp[1][0] = -float('inf')
for i in range(2):
    for j in range(0, n):
        dp[0][j+1] = max(dp[0][j] + a[j], dp[1][j] - a[j])
        dp[1][j+1] = max(dp[0][j] - a[j], dp[1][j] + a[j])

print(dp[0][n])
'''
