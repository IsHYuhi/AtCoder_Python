from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
visited = [False]*n
graph = [[] for i in range(n)]

for i in range(m):
    c, d = map(int, input().split())
    graph[c-1].append(d-1)
    graph[d-1].append(c-1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    ans = []
    while q:
        now = q.popleft()
        ans.append(now)
        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

    return ans

for v in range(n):

    if visited[v] == False:
        nodes = bfs(v)

        if sum(a[idx] for idx in nodes) != sum(b[idx] for idx in nodes):
            print('No')
            exit()

print('Yes')

