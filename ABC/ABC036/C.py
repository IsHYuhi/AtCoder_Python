from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]

count = Counter(a)
sort = sorted(count.items(), key=lambda x: x[0])
dic = {}

for i, (k, v) in enumerate(sort):
    dic[k] = i

for ai in a:
    print(dic[ai])
