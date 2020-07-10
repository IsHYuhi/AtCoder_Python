from collections import deque
o = deque(list(input()))
e = deque(list(input()))
while e:
    print(o.popleft(), end='')
    print(e.popleft(), end='')

if o:
    print(o.popleft(), end='')
print('')