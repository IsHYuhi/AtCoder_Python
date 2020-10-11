n, k = map(int, input().split())
a = list(map(int, input().split()))

triplet = sum(a[:k])
ans = sum(a[:k])
for i in range(k, n):
    triplet += a[i]-a[i-k]
    ans += triplet
print(ans)
