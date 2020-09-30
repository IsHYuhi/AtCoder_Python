X, Y = map(int,input().split())

if Y>4*X or Y<2*X:
    print('No')
elif Y%2!=0:
    print('No')
else:
    print('Yes')