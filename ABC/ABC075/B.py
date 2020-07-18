h, w = map(int, input().split())
field = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if field[i][j] == '.':
            count = 0
            for s in range(max(0,i-1), min(h,i+2)):
                for t in range(max(0,j-1), min(w,j+2)):
                    if field[s][t]=='#':
                        count += 1
            field[i][j] = count
        print(field[i][j], end='')
    print()
