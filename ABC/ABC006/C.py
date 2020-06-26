import itertools
N, M = map(int, input().split())

def combi(t):
    for i in range(0,N+1):
        c = M - i*4 - t*3
        if c%2 != 0 or c<0:
            continue
        else:
            c = c//2
        if c+t+i== N:
            print(c, t, i)
            exit()
    return

combi(0)
combi(1)
print(-1, -1, -1)



# l1 = [i for i in range(1, min(M//2, N)+1)]
# l2 = [i for i in range(1, min(M//3, N)+1)]
# l3 = [i for i in range(1, min(M//4, N)+1)]
# p = itertools.product(l1, l2, l3)

# for i in p:
#     if i[0]*2 + i[1]*3 + i[2]*4 == M and sum(i)<=N:
#         print(i[0], i[1], i[2])
#         exit()
# print(-1, -1, -1)




# def dfs(i, j, k):
#     if i+j+k <= N:
#         if i*2 + j*3 + k*4 == M:
#             print(i, j, k)
#             exit()
#         else:
#             return False
#     else:
#         _ = dfs(i+1, j, k)
#         _ = dfs(i, j, k+1)
#     return False

# print (b, t, f)
# if dfs(0, 0, 0)==False:
#     if dfs(0, 1, 0)==False:
#         print(-1, -1, -1)



