import math
x = int(input())

if x<=6:
    print(1)
elif x<=11:
    print(2)
else:
    ans = (x//11)*2
    res = (x%11)
    if res==0:
        res =0
    elif res<=6:
        res = 1
    elif res<=11:
        res = 2
    print(ans+res)
