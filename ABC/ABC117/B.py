n = int(input())
l = list(map(int, input().split()))
if sum(l)>2*max(l):
    print('Yes')
else:
    print('No')
