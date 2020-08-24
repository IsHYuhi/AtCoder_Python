import math
a, b = map(int, input().split())
n = 1
ans = 0
while n<b:
    for i in range(1, n+1):
        n += a-1
        ans += 1
        if n>=b:
            break
print(ans)