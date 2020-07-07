w, h, n = map(int, input().split())
field = [[1] * w for _ in range(h)]
for i in range(n):
    x, y, a = map(int,input().split())
    if a == 1:
        for i in range(h):
            for j in range(x):
                field[i][j] = 0
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                field[i][j] = 0
    elif a == 3:
        for i in range(y):
            for j in range(w):
                field[i][j] = 0
    elif a == 4:
        for i in range(y,h):
            for j in range(w):
                field[i][j] = 0

count = 0
for i in field:
    count += i.count(1)
print(count)
