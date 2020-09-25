import math

n = int(input())
towns = [list(map(int, input().split())) for _ in range(n)]
ans = 0
c = 0
for i in range(n-1):
    x1, y1 = towns[i]
    for j in range(i+1, n):
        x2, y2 = towns[j]
        ans += math.sqrt((x1-x2)**2 + (y1-y2)**2)*(n-1)*2

print(ans/((n-1)*n))