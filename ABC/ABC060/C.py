n, t = map(int, input().split())
ts = list(map(int, input().split()))

ans = 0
now = 0
for i in ts[1:]:
    if i<=now+t:
        ans += i-now
    else:
        ans += t
    now = i
print(ans+t)