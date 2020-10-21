n, m = map(int, input().split())
ab = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)

low = [float('inf')]*(n+1)
ans = 0

def dfs(i, pre, count):
    global low
    global ans

    low[i] = count
    minlow = low[i]

    for j in ab[i]:
        if j != pre:
            if low[j] == float('inf'):
                dfs(j, i, count+1)
            minlow = min(low[j], minlow)

        if low[j]==count+1:
            ans +=1

    low[i] = minlow

dfs(1, -1, 1)
print(ans)