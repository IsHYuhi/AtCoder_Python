import math
n = int(input())


x, y = 0, 0
ans = float('inf')
for i in range(1, n+1):
    for j in range(i, n+1):
        if i*j>n:
            break
        ans = min(ans, n-i*j+abs(i-j))
print(ans)