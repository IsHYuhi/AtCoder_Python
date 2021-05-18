a = list(map(int, input().split()))
a.sort()
if a[1]-a[0] == a[2]-a[1]:
    print('Yes')
else:
    print('No')
