n, m = map(int, input().split())

ab = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    ab[a-1].append(b)
    ab[b-1].append(a)

for i in ab[0]:
    if n in ab[i-1]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')