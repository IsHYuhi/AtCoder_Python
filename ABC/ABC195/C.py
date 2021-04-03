import math
n = int(input())
p = int(math.log10(n))
ans = 0
for i in range(3, 16, 3):
    if p>=i:
        ans += n-10**i+1
print(ans)