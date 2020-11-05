from collections import Counter
from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]

a_count = Counter(a)
a = [[key, value] for value, key in a_count.items()]
a.sort(reverse=True, key=lambda x: x[1])
a = deque(a)

bc.sort(reverse=True, key=lambda x: x[1])
bc = deque(bc)

ans = 0
count = 0

while count<n or (bc and a):

    if bc:
        bc_n, bc_v = bc[0]
    else:
        bc_n, bc_v = 0, 0

    if a:
        a_n, a_v = a[0]
    else:
        a_n, a_v = 0, 0

    if a_v >= bc_v:
        a.popleft()
        if n-count<a_n:
            a_n = n-count
        count += a_n
        ans += a_n*a_v

    else:
        bc.popleft()
        if n-count<bc_n:
            bc_n = n-count
        count += bc_n
        ans += bc_n*bc_v

print(ans)