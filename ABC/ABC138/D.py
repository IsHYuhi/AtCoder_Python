n, q = map(int, input().split())

ab =[[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

px = [list(map(int, input().split())) for _ in range(q)]
costs = [0]*n
for p, x in px:
    costs[p-1] += x

visited = [0]*n
# parents = [float('inf')]*n
# leaf = [0]*n
counter = [0]*n
stack = []
def dfs(start):
    stack.append(start)
    while stack:
        idx = stack.pop()
        counter[idx] += costs[idx]
        visited[idx] = 1
        flg = False

        for next in ab[idx]:
            if not visited[next]:
                # parents[next] = idx
                stack.append(next)
                counter[next] += counter[idx]
                flg = True

        # if not flg:
        #     leaf[idx] = 1

dfs(0)
# print('visited', visited)
# print('parents', parents)
# print('leaf', leaf)
print(' '.join(map(str, counter)))