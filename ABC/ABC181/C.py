from itertools import combinations
n = int(input())
li = [i for i in range(n)]
xy = [list(map(int, input().split())) for _ in range(n)]
comb = combinations(li, 3)

for i, j, k in comb:
    if (xy[i][1]-xy[j][1])*(xy[k][0]-xy[j][0]) == (xy[k][1]-xy[j][1])*(xy[i][0]-xy[j][0]):
        print('Yes')
        exit()
print('No')