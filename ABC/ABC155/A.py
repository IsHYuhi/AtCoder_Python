a, b, c = map(int, input().split())

if (a==b and c!=a) or (a==c and b!=c) or (b==c and a!=b):
    print('Yes')
else:
    print('No')
