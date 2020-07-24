n = int(input())

def dfs(total):
    if total>=n:
        if total==n:
            print('Yes')
            exit()
        return
    dfs(total+4)
    dfs(total+7)

dfs(0)
print('No')