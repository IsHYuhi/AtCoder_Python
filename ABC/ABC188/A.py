x, y = map(int, input().split())

if min(x, y) + 3 >max(x, y):
    print('Yes')
else:
    print('No')