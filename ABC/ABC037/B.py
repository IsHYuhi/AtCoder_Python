n, q = map(int, input().split())
lrt = [list(map(int, input().split())) for _ in range(q)]
sequence = [0]*n

for l, r, t in lrt:
    sequence[l-1:r] = [t]*(r-l+1)

for i in sequence:
    print(i)
