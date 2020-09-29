n = int(input())
x = list(map(int, input().split()))
ans = float('inf')
mxi = min(x)
mxa = max(x)
for p in range(mxi, mxa+1):
    sm = 0
    for xi in x:
        sm += (xi-p)**2
    ans = min(ans, sm)
print(ans)