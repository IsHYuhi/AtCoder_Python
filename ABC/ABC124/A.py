a, b = map(int, input().split())

if a==b:
    print(a+b)
else:
    print(2 * max(a, b) - 1)