#Accepted with PyPy3(7.3.0)
#Wrong Answer with Python3(3.8.2)

import heapq

class Edge():
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

class Pair():
    def __init__(self, first, second):#first: 最短距離, second: 頂点番号
        self.first = first
        self.second = second

    def __lt__(self, other):
        return (self.first ,self.second) < (other.first, other.second)

def dijkstra(s):
    heapq.heapify(que)
    d[s] = 0
    token[s] = 0
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
                token[e.to] = v
                heapq.heappush(que, Pair(d[e.to], e.to))

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a-1].append(Edge(b-1, 1))
    G[b-1].append(Edge(a-1, 1))

d = [float('inf')]*n
token = [0]*n
que = []
dijkstra(0)

if float('inf') not in d:
    print('Yes')
    for i in range(1, n):
        print(token[i]+1)
else:
    print('No')