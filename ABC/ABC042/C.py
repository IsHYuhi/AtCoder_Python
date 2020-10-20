n, k = map(int, input().split())
d = list(map(int, input().split()))

use = [str(i) for i in range(10) if i not in d]
ans = 99999

def dfs(i, nums):
    global ans
    if i >= 5:
        return nums

    for j in range(len(use)):
        cost = dfs(i+1, use[j]+nums)
        cost_pre = use[j]+nums
        if int(cost)>=n:
            ans = min(ans, int(cost))
        if int(cost_pre)>=n:
            ans = min(ans, int(cost_pre))

    return str(ans)

nums = ''
print(dfs(0, nums))
