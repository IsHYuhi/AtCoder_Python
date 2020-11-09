n = int(input())
a = list(map(int, input().split()))

q = [0]*n
m = max(0, a[0])
q[0] = m
p = [0]*n
p[0] = a[0]

for i in range(1, n):
    p[i] = p[i-1] + a[i]
    if p[i] >= m:
        m = p[i]
    q[i] = m

r = 0
x = 0
for i in range(n):
    r = max(r, x+q[i])
    x = x+p[i]
print(r)