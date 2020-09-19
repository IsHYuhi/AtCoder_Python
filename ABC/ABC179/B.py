n = int(input())

d = [list(map(int, input().split())) for i in range(n)]
count = 0
for i, j in d:
    if i==j:
        count += 1
    else:
        count = 0

    if count>=3:
        print('Yes')
        exit()
print('No')