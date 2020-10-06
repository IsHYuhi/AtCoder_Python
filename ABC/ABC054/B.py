n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]
flag = True
for i in range(n-m+1):
    for j in range(n-m+1):
        flag = True
        for k in range(m):
            for l in range(m):
                if b[k][l] != a[i+k][j+l]:
                    flag = False
                    break
        if flag:
            print('Yes')
            exit()
print('No')
