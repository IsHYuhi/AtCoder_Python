from collections import deque

n, m = map(int, input().split())
x, y = map(int, input().split())

a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

where = 'a'
time = 0
ans = 0

while (a and where=='a') or (b and where=='b'):
    if where=='a':
        flight = a.popleft()
        if flight>=time:
            time = flight + x
            where = 'b'

    elif where=='b':
        flight = b.popleft()
        if flight>=time:
            time = flight + y
            where = 'a'
            ans += 1

print(ans)