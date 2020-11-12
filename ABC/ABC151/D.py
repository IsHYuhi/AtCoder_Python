from collections import deque
import copy
h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]

ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for j in range(h):
    for k in range(w):

        if field[j][k] == '#':
            continue

        d = [[float('inf')]*w for _ in range(h)]
        que = deque([(j, k)])
        d[j][k] = 0
        x, y = j, k
        while que:
            x, y = que.popleft()
            for i in range(4):
                if 0<=x+dx[i]<h and 0<=y+dy[i]<w and field[x+dx[i]][y+dy[i]]=='.' and d[x+dx[i]][y+dy[i]] == float('inf'):
                    que.append((x+dx[i], y+dy[i]))
                    d[x+dx[i]][y+dy[i]] = d[x][y]+1

        ans = max(ans, d[x][y])

print(ans)