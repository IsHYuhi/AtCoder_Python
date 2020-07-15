from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))
a = [list(x) for x in a.items() if x[1]>=2]
a.sort(reverse=True, key=lambda x: (x[0], x[1]))
count = 0
base = 4
for i in range(len(a)):
    if count == 1:
        print(l*a[i][0])
        exit()
    else:
        l = a[i][0]
        count += 1

    if a[i][1]>=4:
        print(a[i][0]*a[i][0])
        exit()

print(0)


