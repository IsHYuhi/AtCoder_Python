from collections import deque
H, W = map(int, input().split())
field = [list(input()) for i in range(H)]
sx, sy, gx, gy = 0, 0, H-1, W-1
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
def bfs():
    d = [[float("inf")] * W for _ in range(H)]
    d[sx][sy] = 0
    Q = deque([])
    Q.append((sx, sy))
    while Q:
        px, py = Q.popleft()
        if px==gx and py==gy:
            break
        for dx, dy in zip(x, y):
            nx = px+dx
            ny = py+dy
            if 0<=nx<H and 0<=ny<W and field[nx][ny]=='.' and d[nx][ny]==float('inf'):
                d[nx][ny]=d[px][py]+1
                Q.append((nx, ny))
    return d[gx][gy]

count = 0
for i in field:
    count += i.count('.')
res = bfs()
if 0 < res < float("inf"):
    print(count-res-1)
else:
    print(-1)