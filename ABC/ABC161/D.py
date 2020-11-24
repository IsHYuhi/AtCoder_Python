k = int(input())

li = []

def dfs(i, s):
    global li
    if i==10:
        li.append(int(s))
        return

    if sum(list(map(int, s)))==0:
        for j in range(10):
            dfs(i+1, s+str(j))
    else:
        for j in range(max(0, int(s[-1])-1), min(10, int(s[-1])+2)):
            dfs(i+1, s+str(j))

dfs(0, '')
li.sort()
print(li[k])