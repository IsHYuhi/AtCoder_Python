import math
n, m = map(int, input().split())

mx = max(n, m)
mn = min(n, m)

if n == m:
    print((2*math.factorial(n)*math.factorial(m))%(10**9+7))
elif n==m-1 or n==m+1:
    print((math.factorial(n)*math.factorial(m))%(10**9+7))
else:
    print(0)