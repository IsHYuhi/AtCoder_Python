v, t, s, d = map(int, input().split())

if v*t <= d <= v*s:
    print('No')
else:
    print('Yes')