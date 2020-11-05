from collections import Counter

n = int(input())
w = [input() for _ in range(n)]

for i in range(n-1):
    if w[i][-1] != w[i+1][0] or w[i+1] in w[:i+1]:
        if i%2 == 0:
            print('WIN')
        else:
            print('LOSE')
        exit()

print('DRAW')
