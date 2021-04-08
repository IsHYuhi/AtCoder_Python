n = int(input())
s = [input() for _ in range(n)]

r = 0
b = 0

for rb in s:
    for color in rb:
        if color == 'R':
            r += 1
        elif color == 'B':
            b += 1
        else:
            continue

if r>b:
    print('TAKAHASHI')
elif r<b:
    print('AOKI')
else:
    print('DRAW')
