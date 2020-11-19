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

n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    v, to, c = map(int, input().split())
    G[v-1].append(Edge(to-1, c))
    G[to-1].append(Edge(v-1, c))

q, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(q)]

d = [float('inf')]*n
que = []
dijkstra(k-1)

for x, y in xy:
    print(d[x-1]+d[y-1])


'''using warshall-floyd is going to be TLE because of O(n^3)'''
# n = int(input())

# d = [[float('inf')]*n for _ in range(n)]
# for i in range(n-1):
#     a, b, c = map(int, input().split())
#     d[a-1][b-1] = c
#     d[b-1][a-1] = c

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if d[i][k]!=float('inf') and d[k][i]!=float('inf'):
#                 d[i][j] = min(d[i][j], d[i][k] + d[k][j])

# q, k = map(int, input().split())
# xy = [list(map(int, input().split())) for _ in range(q)]

# for x, y in xy:
#     print(d[x-1][k-1]+d[k-1][y-1])
