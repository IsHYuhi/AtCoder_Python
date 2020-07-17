a, b, c, d = map(int, input().split())
l = a+b
r = c+d
if l==r:
    print('Balanced')
elif l>r:
    print('Left')
else:
    print('Right')