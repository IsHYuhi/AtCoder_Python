W, a, b = map(int, input().split())

if a<=b<=a+W:
    print(0)
else:
    print(min(abs(b - a+W), abs(a- b+W)))