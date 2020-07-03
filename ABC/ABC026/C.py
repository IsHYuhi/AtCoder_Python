n = int(input())
table = [[] for i in range(n+1)]

for i in range(2,n+1):
    j = int(input())
    table[j].append(i)

def dfs(chi):
    _max = 0
    _min = float('inf')
    if not chi:
        return 1

    for j in chi:
        num = dfs(table[j])
        _max = max(_max, num)
        _min = min(_min, num)
    return _max+_min+1

print(dfs(table[1]))