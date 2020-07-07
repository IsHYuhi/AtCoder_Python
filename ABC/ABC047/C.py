from collections import deque
S = deque(list(input()))

ans = 0
s = S.popleft()
while S:
    n = S.popleft()
    if s != n:
        ans += 1
        s = n
print(ans)
