from collections import deque
s = deque(input())
q = int(input())
query = [list(input().split()) for _ in range(q)]

reverse = 0# 3 or 0

for i in range(q):
    if int(query[i][0]) == 1:
        reverse = abs(reverse-3)
    else:
        if abs(int(query[i][1])-reverse) == 1:
            s.appendleft(query[i][2])
        else:
            s.append(query[i][2])

if reverse:
    s = list(s)[::-1]
else:
    s = list(s)

print(''.join(list(map(str,s))))
