n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
i = -2
for j in range(n):
    if a[j]-1 == i+1:
        ans += c[i]
    i = a[j] - 1
    ans += b[i]
print(ans)
