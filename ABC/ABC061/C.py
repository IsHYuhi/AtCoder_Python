n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
sm = 0
for a, b in ab:
    sm += b
    if sm >= k:
        print(a)
        break

