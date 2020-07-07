from collections import Counter
a = list(map(int, input().split()))

a = Counter(a)

if a.get(7) and a.get(5):
    if a[7]==1 and a[5]==2:
        print('YES')
        exit()
print('NO')

