n = int(input())
sn = list(map(int, list(str(n))))
if n%sum(sn)==0:
    print('Yes')
else:
    print('No')