n = int(input())
a = list(map(int, input().split()))

print(a.index(min(max(a[:2**(n-1)]), max(a[2**(n-1):]))) + 1)
