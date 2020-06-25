import itertools

N, M = map(int, input().split())
xy = [[0]*N for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -=1
    y -=1
    xy[x][y] = 1
    xy[y][x] = 1
#xy = [list(map(int, input().split())) for i in range(M)]
#print(xy)

ans = 0

def dfs(i, group):
    global ans
    if i == N:
        flag = True
        for i in itertools.combinations(group, 2):
            if xy[i[0]][i[1]] == 0:
                flag = False
                break
        if flag:
            ans = max(ans, len(group))
    else:
        dfs(i+1, group)
        dfs(i+1, group + [i])


dfs(0, [])
print(ans)