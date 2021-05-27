# AC with PyPy3
r, c, k_ = map(int, input().split())
field = [list(map(lambda x: True if x=='o' else False ,list(input()))) for _ in range(r)]

for k in range(k_-1):
    new_field = [[False]*c for _ in range(r)]
    for i in range(0, r):
        for j in range(0, c):
            if i == 0 or j == 0 or i == r-1 or j == c-1:
                new_field[i][j] = False
            else:
                new_field[i][j] = field[i+1][j] and field[i][j+1] and field[i][j] and field[i-1][j] and field[i][j-1]

    for i in range(0, r):
        for j in range(0, c):
            field[i][j] = new_field[i][j]
print(sum([sum(field[i]) for i in range(r)]))

# xy = []
# for i in range(k, r-k+2):
#     for j in range(k, c-k+2):
#         xy.append([i, j])
# # print(xy)

# ans = 0
# for x, y in xy:
#     flag = 1
#     for i in range(x-k, x+k):
#         for j in range(y-k, y+k):
#             if abs(i+1-x)+abs(j+1-y) > k-1:
#                 continue
#             if i<0 or i>r-1 or j<0 or j>c-1:
#                 flag = 0
#                 break
#             if field[i][j]=='x':
#                 flag = 0
#                 break

#         if flag == 0:
#             break

#     if flag == 1:
#         ans += 1

# print(ans)


# for i in range(r):
#     for j in range(c):
#         for k in range(min(0, j-k))
