import math

def fac(n):
    num = 0
    for i in range(1, n+1):
        num += n-i+1
    return num

n = int(input())
a = list(map(int, input().split()))
ans = 0
count = 0
p = -1

for i in range(n):
    if p < a[i]:
        count += 1
    else:
        ans += fac(count)
        count = 1

    p = a[i]

print(ans+fac(count))
