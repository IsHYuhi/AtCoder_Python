n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_as = [0]
sum_bs = [0]

for i in range(n):
    sum_as.append(sum_as[i]+a[i])
for i in range(m):
    sum_bs.append(sum_bs[i]+b[i])

ans = 0
i = 0
j = m

while i<=n and sum_as[i] <= k:
    while sum_bs[j] > k-sum_as[i]:
        j -= 1
    ans = max(ans, i+j)
    i += 1
print(ans)
