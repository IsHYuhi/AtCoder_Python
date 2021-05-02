from collections import deque
s = list(input())
t = deque([])
reverse = False
for i in s:
    if i == 'R':
        reverse = True if reverse == False else False
        continue

    if reverse:
        t.appendleft(i)
    else:
        t.append(i)

if reverse:
    t.reverse()

if not t:
    print()
    exit()
ans = [t.popleft()]
while t:
    ans.append(t.popleft())
    if len(ans)>=2:
        if ans[-2] == ans[-1]:
            ans.pop()
            ans.pop()

print(''.join(ans))
