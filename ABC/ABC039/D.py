h, w = map(int, input().split())
img = [list(input()) for _ in range(h)]
morph = [['']*w for _ in range(h)]
rest = [['']*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        flag = True

        if img[i][j] == '.':
            morph[i][j] = '.'
            continue

        for dh in range(-1, 2):
            for dw in range(-1, 2):
                if 0<=i+dh<h and 0<=j+dw<w:
                    if img[i+dh][j+dw] == '.':
                        flag = False
                        break
            if flag == False:
                break

        if flag:
            morph[i][j] = '#'
        else:
            morph[i][j] = '.'

possibility = True
for i in range(h):
    for j in range(w):
        flag = False

        if morph[i][j] == '#':
            rest[i][j] = '#'
            continue

        for dh in range(-1, 2):
            for dw in range(-1, 2):
                if 0<=i+dh<h and 0<=j+dw<w:
                    if morph[i+dh][j+dw] == '#':
                        flag = True
                        break
            if flag == True:
                break

        if flag:
            rest[i][j] = '#'
        else:
            rest[i][j] = '.'

        if rest[i][j] != img[i][j]:
            possibility = False

if possibility:
    print('possible')
    for i in range(h):
        print(''.join(morph[i]))
else:
    print('impossible')
