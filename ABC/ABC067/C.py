from collections import deque
n = int(input())
a = deque(list(map(int, input().split())))
ans = float('inf')
total = sum(a)
sm = 0
while len(a)>1:
    sm += a.pop()
    ans = min(abs(2*sm-total), ans)
print(ans)