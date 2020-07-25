from collections import Counter
n = int(input())
w = [input() for _ in range(n)]

if n != len(Counter(w)):
    print('No')
    exit()

s = w[0][-1]
for i in range(1,n):
    if s != w[i][0]:
        print('No')
        exit()
    s = w[i][-1]
print('Yes')