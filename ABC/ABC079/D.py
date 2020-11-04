import heapq

class Edge():
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

class Pair():
    def __init__(self, first, second):
        #first: 最短距離, second: 頂点番号
        self.first = first
        self.second = second

    def __lt__(self, other):
        return (self.first ,self.second) < (other.first, other.second)

def dijkstra(s):
    heapq.heapify(que)
    d[s] = 0
    heapq.heappush(que, Pair(0, s))

    while que:
        p = heapq.heappop(que)
        v = p.second
        if d[v] < p.first:
            continue
        for i in range(len(G[v])):
            e = G[v][i]
            if d[e.to] > d[v] + e.cost:
                d[e.to] = d[v] + e.cost
                heapq.heappush(que, Pair(d[e.to], e.to))


h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]

G = [[] for _ in range(10)]
for i, row in enumerate(c):
    for j, cost in enumerate(row):
        G[i].append(Edge(j, cost))

field = [list(map(int, input().split())) for _ in range(h)]
costs = []

for i in range(10):
    d = [float('inf')]*10
    que = []
    dijkstra(i)
    costs.append(d[1])

ans = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == -1:
            continue
        ans += costs[field[i][j]]

print(ans)