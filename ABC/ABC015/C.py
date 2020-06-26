N, K = map(int, input().split())
T = [list(map(int, input().split()))for i in range(N)]

def dfs(i, x):
    if i == N:
        if x == 0:
            return True
    else:
        for k in range(K):
            if dfs(i+1, x ^ T[i][k]):
                return True
        return False

if dfs(0, 0):
    print("Found")
else:
    print("Nothing")