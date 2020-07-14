import math
n = int(input())
a = list(map(int, input().split()))
c2 = 0
c4 = 0
for i in a:
    if i%4==0:
        c4+=1
    elif i%2==0:
        c2+=1

if c2 == len(a):
    print('Yes')
elif c2 >= 2:
    if c4 >= (math.ceil((len(a)-c2)/2)):
        print('Yes')
    else:
        print('No')
elif c4 >=(len(a)//2):
    print('Yes')
else:
    print('No')