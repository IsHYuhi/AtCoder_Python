from itertools import combinations
n, m = map(int, input().split())
ksm = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

onoff = [0]*n
total = 0

def dfs(i, onoff):
    global total
    if i == n:
        flag = True
        for idx, j in enumerate(ksm):
            count = 0
            for k in j[1:]:
                count += onoff[k-1]
            if count%2 != p[idx]:
                flag = False
        if flag:
            total += 1
        return
    dfs(i+1, onoff[:])
    dfs(i+1, onoff[:i]+[1]+onoff[i+1:])

dfs(0, onoff)
print(total)