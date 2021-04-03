n = int(input())
apx = [list(map(int, input().split())) for _ in range (n)]
m = float('inf')
for a, p, x in apx:
    if x-a > 0:
        m = min(m, p)

m = -1 if m == float('inf') else m
print(m)