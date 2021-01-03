n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
l = len(xy)
ans = 0
for i in range(l):
    xi, yi = xy[i][0], xy[i][1]
    for j in range(i+1, l):
        xj, yj = xy[j][0], xy[j][1]

        a = abs((yi-yj)/(xi-xj))
        if a <= 1:
            ans += 1

print(ans)