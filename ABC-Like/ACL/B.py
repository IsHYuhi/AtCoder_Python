a, b, c, d = map(int, input().split())

if min(b,d) - max(a, c) >= 0:
    print('Yes')
else:
    print('No')