n = int(input())
a = list(map(int, input().split()))
m = a[0]
ans = 0
for i in a:
    if m > i:
        ans += m - i
    else:
        m = i
print(ans)
