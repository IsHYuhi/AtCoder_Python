from operator import itemgetter
N, M = map(int, input().split())
ab = sorted([tuple(map(int, input().split())) for i in range(M)], key=itemgetter(1))

ans = 0
removed = -1

for a, b in ab:
    if a > removed:
        removed = b-1
        ans += 1
print(ans)