from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))
a = [[i, j] for i, j in a.items()]

ans = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        ans += (a[i][1]*a[j][1])*(a[i][0]-a[j][0])**2

print(ans)