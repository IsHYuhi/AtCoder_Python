n = int(input())

testimony = []
a_s = []

for _ in range(n):
    a = int(input())
    a_s.append(a)
    test = [list(map(int, input().split())) for _ in range(a)]
    testimony.append(test)

def check(testimony, flags):
    check_list = [-1]* len(testimony)
    for i in range(n):
        if not flags[i]:
            continue
        for j in range(a_s[i]):
            if (testimony[i][j][1]==0 and flags[testimony[i][j][0]-1] == True) or (testimony[i][j][1]==1 and flags[testimony[i][j][0]-1] == False):
                return False

    return True

def dfs(i, testimony, total, flags):
    if i == n:
        if check(testimony, flags):
            return total
        else:
            return 0

    ans_f = dfs(i+1, testimony, total, flags[:])

    next_testimony = testimony.copy()
    for j in range(a_s[i]):
        if next_testimony[i][j][1] == 0:
            flags[next_testimony[i][j][0]-1] == False

    next_flags = flags.copy()
    next_flags[i] = True
    ans_t = dfs(i+1, next_testimony, total+1, next_flags)

    ans = max(ans_t, ans_f)

    return ans

flags = [False]*n
ans = dfs(0, testimony, 0, flags)
print(ans)