from collections import deque
S = input()
S = deque(S)
s = S.popleft()
count = 1
while S:
    t = S.popleft()
    if t == s:
        count+=1
    else:
        print(s+str(count), end='')
        count = 1
    s = t
print(s+str(count))
