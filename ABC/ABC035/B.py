from collections import Counter
s = input()
t = int(input())

s = Counter(s)
move = ['L', 'R', 'U', 'D']
x = y = 0
for d in move:
    if s.get(d):
        if d == 'L':
            x -= s.get(d)
        elif d == 'R':
            x += s.get(d)
        elif d == 'U':
            y += s.get(d)
        elif d == 'D':
            y -= s.get(d)

if s.get('?'):
    q = s.get('?')
if t==1:
    print(abs(x)+abs(y)+q)
else:
    if 0<abs(x)+abs(y)<q:
        print((q-(abs(x)+abs(y)))%2)
    elif 0 == abs(x)+abs(y):
        print((q%2))
    else:
        print(abs(x)+abs(y)-q)