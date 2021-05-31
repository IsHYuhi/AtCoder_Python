from collections import deque
n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ab = deque(ab)

while ab:
    a_, b_ = ab.popleft()
    if a_<=k:
        k += b_
    else:
        print(k)
        exit()

print(k)
