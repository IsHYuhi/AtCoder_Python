n = int(input())
ab = []
now = 0
for i in range(n):
    _a, _b = map(int, input().split())
    ab.append([_a, _b])

ab.sort(key=lambda x: x[1])
for a, b in ab:
    now += a
    if now>b:
        print('No')
        exit()
print('Yes')