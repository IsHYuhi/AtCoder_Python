from operator import itemgetter
n = int(input())
x = list(map(int, input().split()))

x = [(j, i) for i, j in enumerate(x)]
x.sort(key=itemgetter(0))

medi1 = x[len(x)//2][0]
medi2 = x[len(x)//2-1][0]
ans = [0]*n

for i in range(len(x)):
    if i<len(x)//2:
        ans[x[i][1]] = medi1
    else:
        ans[x[i][1]] = medi2

for a in ans:
    print(a)
