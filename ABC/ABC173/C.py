h, w, k = map(int,input().split())

field = [list(input()) for i in range(h)]

ans = 0
for maskr in range(0, 1<<h):#1のhビット左シフト2^h
    for maskc in range(0, 1<<w):
        black = 0
        for i in range(h):
            for j in range(w):
                if ((maskr>>i) & 1) == 0 and ((maskc>>j) & 1) == 0 and field[i][j] == '#':
                    #mask>>i: maskrのiビット右シフト2^(-i), つまりi番目が1じゃない(赤く塗られていない)かどうかを調べている
                    #赤く塗られていないかつ、#ならblackとしてカウント, 2^h * 2^w　通り、つまり2^(h+w)通り全探索している
                    black +=1
        if black == k:
            ans += 1
print(ans)
