n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

def check(dishes):
    count = 0
    fill = [0]*n
    for i in dishes:
        fill[i-1] = 1
    for a, b in ab:
        if fill[a-1] and fill[b-1]:
            count += 1
    return count


def dfs(li, i):
    if i >= k:
        return check(li)

    left = dfs(li+[cd[i][0]], i+1)
    right = dfs(li+[cd[i][1]], i+1)

    ans = max(left, right)

    return ans

print(dfs([], 0))
