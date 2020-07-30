n, m = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(m)]
l = 1
r = n
for i, j in lr:
    l = max(i, l)
    r = min(j, r)
print(max(r-l+1, 0))
