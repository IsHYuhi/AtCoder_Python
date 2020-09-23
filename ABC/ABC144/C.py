import math
n = int(input())
ans = float('inf')
for i in range(1, int(math.sqrt(n)+1)):
    if n%i==0:
        ans = min(i + n//i - 2, ans)
print(ans)
