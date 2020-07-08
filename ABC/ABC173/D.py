from collections import deque
n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
#最大値が1回, それ以降は大きい順に2回ずつ関わる.
for i in range(1, n):
    ans += a[n-i//2-1]
print(ans)