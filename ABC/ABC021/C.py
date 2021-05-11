from collections import Counter
n = int(input())
a, b = map(int, input().split())
m =int(input())
xy = [list(map(int, input().split())) for _ in range(m)]

def topsort(G):
    Q = []
    count = dict((u, 0) for u in range(len(G)))

    for u in range(len(G)):
        for v in G[u]:
            count[v] += 1

    for u in range(len(G)):
        if count[u] == 0:
            Q.append(u)
    anslst = []
    while Q:
        u = Q.pop()
        anslst.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)


    anslst.reverse()
    return anslst

v = n

d = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    d[i][i] = 0

for x, y in xy:
    d[x-1][y-1] = 1
    d[y-1][x-1] = 1

for k in range(v):
    for i in range(v):
        for j in range(v):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

#warshall-floyd
graph = [[] for _ in range(n)]
s = d[a-1]
for x, y in xy:
    if s[x-1]+1 == s[y-1]:
        graph[y-1].append(x-1)
    if s[y-1]+ 1 == s[x-1]:
        graph[x-1].append(y-1)

#topological sort
lst = topsort(graph)

#dp
mod = 10**9+7
dp = [0] * n
dp[a-1] = 1
for i in lst:
    if i == a-1:
        continue
    for u in graph[i]:
        dp[i] += dp[u]
        dp[i] %= mod
print(dp[b-1])
