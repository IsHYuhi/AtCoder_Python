a, b, c, x, y = map(int, input().split())

if x==y:
    each = 0
elif x>y:
    each = min(a, 2*c)*(x-y)
else:
    each = min(b, 2*c)*(y-x)

print(min(min(x, y)*2*c+each, min(a, 2*c)*x + min(b, 2*c)*y))
