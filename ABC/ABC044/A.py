n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(min(n, k)*x+max(n-k, 0)*y)