n = int(input())
w = list(map(int, input().split()))
ans = float('inf')
s1 = 0
s2 = sum(w)
for t in range(0,n):
    s1 += w[t]
    s2 -= w[t]
    ans = min(ans, abs(s1-s2))
print(ans)
