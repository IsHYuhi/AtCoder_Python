A = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
cdl = 0
cdr = 0
for i in range(3):
    cr = 0
    cc = 0
    for j in range(3):
        if A[i][j] in b:
            cr += 1
        if A[j][i] in b:
            cc += 1
        if i == j and A[i][j] in b:
            cdl += 1
        if i+j==2 and A[i][j] in b:
            cdr += 1

    if cr == 3 or cc == 3 or cdl == 3 or cdr ==3:
        print('Yes')
        exit()
print('No')