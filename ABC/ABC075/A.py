from collections import Counter
a = Counter(list(map(int, input().split())))
a = [i[0] for i in a.items() if i[1]==1]
print(a[0])
