n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = list(tuple(map(int,input().split())) for _ in range(m))

for p, x in px:
    ts = t.copy()
    ts[p-1] = x
    print(sum(ts))