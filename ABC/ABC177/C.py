n = int(input())
a = list(map(int, input().split()))

sm = sum(a)
ans = 0

for i in range(len(a)):
    ans += a[i]*(sm-a[i])
    sm = sm - a[i]
    ans %= (10**9)+7
print(ans)