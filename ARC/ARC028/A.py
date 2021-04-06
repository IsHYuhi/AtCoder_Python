n, a, b = map(int, input().split())

if 0<n%(a+b)<=a:
    print('Ant')
else:
    print('Bug')