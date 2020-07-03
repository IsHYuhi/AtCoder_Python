import math
n, m = map(int, input().split())
if n>=12:
    n = n-12
n = (60*n + m)/2
m = 6*m
ans = abs(m-n)
print(min(ans, 360-ans))