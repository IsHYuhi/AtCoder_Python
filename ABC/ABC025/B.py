N, A, B = map(int, input().split())
position = 0
for i in range(N):
    s, d = input().split()
    d = int(d)
    if d<A:
        d = A
    elif d>B:
        d = B
    if s == 'West':
        position -= d
    elif s == 'East':
        position += d

if position<0:
    print('West', abs(position))
elif position>0:
    print('East', abs(position))
else:
    print(0)