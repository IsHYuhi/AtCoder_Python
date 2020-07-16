n = int(input())
d = list(map(int, list(str(n))))

if n%sum(d)==0:
    print('Yes')
else:
    print('No')
