## AC only with PyPy3
n, x, y = map(int, input().split())
d = [[float('inf')]*n for _ in range(n)]
tree = [[] for _ in range(n)]

i = 0
for i in range(n-1):
    tree[i].append(i+1)
    tree[i+1].append(i)
tree[x-1].append(y-1)
tree[y-1].append(x-1)


def dfs(i_, cost_, k_):
    global d
    stack = []
    stack.append((i_, cost_, k_))
    while stack:
        i, cost, k = stack.pop()
        if d[k][i] != float('inf') and d[k][i] < cost:
            continue
        d[k][i] = min(d[k][i], cost)
        for j in tree[i]:
            stack.append((j, d[k][i]+1, k))
            #dfs(j, d[k][i]+1, k)

for k in range(n):
    dfs(k, 0, k)

ans = [0]*n
for i in range(n):
    for j in range(i, n):
        ans[d[i][j]] += 1

for i in range(1, n):
    print(ans[i])