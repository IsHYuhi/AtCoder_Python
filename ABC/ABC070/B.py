a, b, c, d = map(int, input().split())
print(max(min(d, b) - max(a, c), 0))