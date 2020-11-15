a, b = map(int, input().split())
if abs(a)<abs(b):
    print('Ant')
elif abs(b)<abs(a):
    print('Bug')
else:
    print('Draw')