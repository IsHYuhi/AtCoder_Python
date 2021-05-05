a, b, c = map(int, input().split())

if min(a, b) <= c <= max(a, b):
    print('Yes')
else:
    print('No')