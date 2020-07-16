x, y = input().split()

if ord(x)<ord(y):
    print('<')
elif ord(x)>ord(y):
    print('>')
else:
    print('=')
