n, h, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

count = 0
for a, b in ab:
    if a>=h and b>=w:
        count += 1
print(count)