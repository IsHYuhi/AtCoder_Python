n, m = map(int, input().split())

abes = [list(map(int, input().split())) for _ in range(n)]
cdes = [list(map(int, input().split())) for _ in range(m)]

for a, b in abes:
    mi = sorted(cdes, key=lambda x : abs(x[0]-a)+abs(x[1]-b))
    print(cdes.index(mi[0])+1)