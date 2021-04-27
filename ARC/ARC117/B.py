n = int(input())
a = list(set(map(int, input().split())))

a.sort(reverse=True)
ans = a[-1]+1
for i in range(len(a)-1):
    ans *= a[i]-a[i+1]+1
    ans %= 10**9+7

print(ans)
