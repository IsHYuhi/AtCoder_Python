from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
field = [list(input()) for i in range(R)]
#print(d)
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def bfs():
    d = [[float('inf')]*C for i in range(R)]
    d[sy-1][sx-1] = 0
    Q = deque([])
    Q.append((sy, sx))
    while Q:
        py, px = Q.popleft()
        if px==gx and py==gy:
            break
        for dy, dx in zip(dys, dxs):
            nowy = py + dy
            nowx = px + dx

            if field[nowy-1][nowx-1]=='.' and 0<=nowx<C and 0<=nowy<R and d[nowy-1][nowx-1] == float("inf"):##範囲外のチェックをする
                d[nowy-1][nowx-1] = d[py-1][px-1] + 1
                Q.append((nowy, nowx))
    return d[gy-1][gx-1]
print(bfs())

# from collections import deque

# def bfs():
#     d = [[float("inf")] * c for i in range(r)]

#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]

#     que = deque([])
#     que.append((sy, sx))
#     d[sy][sx] = 0

#     while que:
#         p = que.popleft()
#         if p[0] == gy and p[1] == gx:
#             break
#         for i in range(4):
#             nx = p[0] + dx[i]
#             ny = p[1] + dy[i]

#             if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
#                 que.append((nx, ny))
#                 d[nx][ny] = d[p[0]][p[1]] + 1

#     return d[gy][gx]


# r, c = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# sx -= 1
# sy -= 1
# gy -= 1
# gx -= 1
# maze = [list(input()) for i in range(r)]

# print(bfs())