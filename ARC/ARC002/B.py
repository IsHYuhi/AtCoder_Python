days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y, m, d = map(int, input().split('/'))

def Apy(y, m):
    if m != 2:
        return days[m-1]
    if (y%4==0 and y%100!=0) or (y%400==0):
        return 29
    else:
        return 28

for i in range(y, 3001):
    for j in range(m, 13):
        for k in range(d, Apy(i, j)+1):
            if (i/j)%k==0:
                print('{:s}/{:s}/{:s}'.format(str(i).zfill(4), str(j).zfill(2), str(k).zfill(2)))
                exit()
        d = 1
    m = 1
