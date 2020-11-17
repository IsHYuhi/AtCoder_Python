import itertools
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
li = [i for i in range(1, n)]
p_list = list(itertools.permutations(li, n-1))

ans = 0
for l in p_list:
    s = 0
    count = 0
    for i in l:
        count += t[s][i]
        s = i
    count += t[s][0]
    if count == k:
        ans += 1

print(ans)