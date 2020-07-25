n, m, x, y = map(int, input().split())
xn = list(map(int, input().split()))
ym = list(map(int, input().split()))

xn = max(xn)
ym = min(ym)

for z in range(x+1,y+1):
    if xn < z <= ym:
        print('No War')
        exit()
print('War')
