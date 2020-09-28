n, k, m = map(int, input().split())
a = list(map(int, input().split()))

ans = max(0, m*n-sum(a)) if m*n-sum(a)<=k else -1
print(ans)