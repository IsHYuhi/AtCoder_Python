n = int(input())
a = list(map(int, input().split()))
s = sum(a)

x = [0]*(n+1)
x[0] = s- 2*sum(a[1::2])
for i in range(n):
    x[i+1] = 2*a[i]-x[i]

print(' '.join(map(str, x[:-1])))
