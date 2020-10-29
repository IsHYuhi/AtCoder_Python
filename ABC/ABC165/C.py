n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

ans = []
def dfs(i, pre, a):
    global ans
    if i >= n:
        ans.append(a)
        return

    for j in range(pre, m+1):
        dfs(i+1, j, a+[j])

dfs(0, 1, [])

answer = 0
for an in ans:
    sum = 0
    for a, b, c, d in abcd:
        if an[b-1]-an[a-1] == c:
            sum += d
    answer = max(sum, answer)

print(answer)