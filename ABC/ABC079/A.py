from collections import deque
n = deque(list(input()))
digit = n.popleft()
cnt = 1
while n:
    if cnt == 3:
        break
    d = n.popleft()
    if d == digit:
        cnt += 1
    else:
        digit = d
        cnt = 1

if cnt == 3:
    print('Yes')
else:
    print('No')