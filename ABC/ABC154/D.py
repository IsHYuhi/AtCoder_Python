n, k = map(int, input().split())
p = list(map(int, input().split()))
total = sum([((p[i]*(p[i]+1))//2)/p[i] for i in range(k)])
ans = total

for i in range(k, n):
    pre = ((p[i-k]*(p[i-k]+1))//2)/p[i-k]
    nxt = ((p[i]*(p[i]+1))//2)/p[i]

    ans = max(ans, total-pre+nxt)
    total = total-pre+nxt

print(ans)