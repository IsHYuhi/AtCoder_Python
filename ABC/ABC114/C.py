n = int(input())

sitigosan = []
def dfs(s):
    global sitigosan
    sitigosan.append(int(s))
    if len(s)>=len(str(n))+1:
        return
    for i in ['3', '5', '7']:
        dfs(s+i)

dfs('0')
sitigosan = sorted(sitigosan)
ans = 0
for i in sitigosan:

    if i>n:
        break

    if len(set(str(i)))>=3:
        ans += 1

print(ans)