a, b, x, y = map(int, input().split())

m = min(y, (x*2))

if a>b:
        print((a-b-1) * m + x)
elif b>a:
    print((b-a) * m + x)
else:
    print(x)