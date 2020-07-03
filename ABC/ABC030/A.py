a, b, c, d = map(int, input().split())
if b/a == d/c:
    print('DRAW')
elif b/a > d/c:
    print('TAKAHASHI')
else:
    print('AOKI')