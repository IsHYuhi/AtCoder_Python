n, k = map(int, input().split())
ans = 1
while n>=k:
    n = n//k
    ans += 1
print(ans)