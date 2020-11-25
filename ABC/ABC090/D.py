n, k = map(int, input().split())
ans = 0

for b in range(1, n+1):
    p = n//b
    ans += p*max(0,b-k)
    r = n%b
    ans += max(0, r-k+1)

offset = 0
if k == 0:
    offset = n
print(ans-offset)
