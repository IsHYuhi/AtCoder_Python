from collections import deque
n = int(input())
v = deque(sorted(list(map(int, input().split()))))
for i in range(n-1):
    v1 = v.popleft()
    v2 = v.popleft()
    v.appendleft((v1+v2)/2)
print(v[0])