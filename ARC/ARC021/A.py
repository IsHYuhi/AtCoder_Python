a = [list(map(int, input().split())) for _ in range(4)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if  0 <= i+dy[k] < 4 and 0 <= j+dx[k] < 4:
                if a[i][j] == a[i+dy[k]][j+dx[k]]:
                    print('CONTINUE')
                    exit()
print('GAMEOVER')