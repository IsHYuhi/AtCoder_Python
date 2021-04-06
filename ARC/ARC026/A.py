n, a, b = map(int, input().split())

print(min(5, n)*b+a*max(n-5, 0))
