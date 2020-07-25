h, w = map(int, input().split())
field =  [list(input()) for i in range(h)]

w_row = ['.' for i in range(w)]
del_row_list = []
del_col_list = []

for i in range(h):
    if field[i] == w_row:
        del_row_list.append(i)

for j in range(w):
    count = 0
    for i in range(h):
        if field[i][j] == '.':
            count += 1
    if count == h:
        del_col_list.append(j)

for i in range(h):
    if i in del_row_list:
        continue
    for j in range(w):
        if j in del_col_list:
            continue
        print(field[i][j], end='')
    print('')
