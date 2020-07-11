n, m = map(int, input().split())

ab =[[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

for i in ab:
    print(len(i))