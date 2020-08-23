from itertools import combinations

n = int(input())
p = list(map(int, input().split()))

combi = combinations([i for i in range(n)], 2)
sort = sorted(p)

if sort == p:
        print('YES')
        exit()

for i, j in combi:
    p[i], p[j] = p[j], p[i]
    if sort == p:
        print('YES')
        exit()
    p[j], p[i] = p[i], p[j]
print('NO')
