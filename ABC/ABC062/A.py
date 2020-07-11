x, y = map(int, input().split())
b = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

if b[x]==b[y]:
    print('Yes')
else:
    print('No')