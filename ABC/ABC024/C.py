n, d, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(d)]
st = [list(map(int, input().split())) for _ in range(k)]
ans = [-1]*k

def min_distance(r, l, s, t):
    if abs(r-st[i][1]) <= abs(l-st[i][1]):
        return r
    else:
        return l


for j, (l, r) in enumerate(lr):
    for i in range(k):#1<=k<=100
        if l<=st[i][0]<=r:
            if l<=st[i][1]<=r and ans[i] == -1:
                ans[i] = j+1
            else:
                st[i][0] = min_distance(l, r, st[i][0], st[i][1])

for a in ans:
    print(a)
