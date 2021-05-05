x, y, z = map(int, input().split())

a = y/x
if a*z-int(a*z) > 0:
    print(int(a*z))
else:
    print(int(a*z)-1)