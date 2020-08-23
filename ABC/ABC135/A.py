a, b = map(int, input().split())

if (max(a,b)-min(a,b))%2 == 0:
    print((max(a,b)-min(a,b))//2+min(a,b))
else:
    print('IMPOSSIBLE')