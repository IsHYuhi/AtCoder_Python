N, M = map(int, input().split())
#ab = [list(map(int, input().split())) for i in range(M)]
ab = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)
#print(ab)

count = 0

def dfs(i, now, done):
    global count
    if i == N-1:
        count += 1
        #print(now+1)
        #print('-----')
        return

    for j in ab[now]:
        #print(j, done)
        if j not in done:
            #print(j+1)
            #done.append(j)
            dfs(i+1, j, done + [j])##引数はバラして入れる！
    return

dfs(0, 0, [0])
print(count)

# import itertools

# n, m = map(int, input().split())

# path = [[False] * n for i in range(n)]
# for i in range(m):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     path[a][b] = True
#     path[b][a] = True

# ans = 0

# for i in itertools.permutations(range(n), n):#N!
#     if i[0] == 0:
#         for j in range(n):
#             if j == n - 1:
#                 ans += 1
#                 break
#             if not path[i[j]][i[j + 1]]:
#                 break

# print(ans)