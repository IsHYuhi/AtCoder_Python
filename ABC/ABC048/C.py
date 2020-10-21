n, x = map(int, input().split())
a = list(map(int, input().split()))

a_org = a.copy()
ans = 0

for i in range(n-1):
        if a[i]+a[i+1] > x:
            if a[i] > x:
                a[i+1] = 0
                a[i] = x
            else:
                a[i+1] = x - a[i]

for i in range(n):
    ans += a_org[i]-a[i]

print(ans)