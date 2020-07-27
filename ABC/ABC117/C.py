import math
n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
ans = 0
l = []
for i in range(m-1):
    l.append(x[i+1]-x[i])
l.sort(reverse=True)
print(x[-1]-x[0]-sum(l[:n-1]))