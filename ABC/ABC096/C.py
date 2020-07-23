h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
count = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == '#':
            count = 0
            for d in range(4):
                if 0<=i+dy[d]<h and 0<=j+dx[d]<w:
                    count += 1 if field[i+dy[d]][j+dx[d]]=='#' else 0

            if count<1:
                print('No')
                exit()
print('Yes')
