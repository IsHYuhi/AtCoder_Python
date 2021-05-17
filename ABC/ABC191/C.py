h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]

move = [(-1, -1), (-1, 0), (0, -1), (0, 0)]
ans = 0
for i in range(1, h):
    for j in range(1, w):
        l = sum([field[i+y][j+x] == '#' for x, y in move])
        if l == 3 or l == 1:
            ans += 1
print(ans)