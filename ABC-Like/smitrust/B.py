import math
n = int(input())
p1 = math.ceil(n*100/108)
p2 = p1 - 1

if int(p1*1.08) == n:
    print(p1)
elif int(p2*1.08) == n:
    print(p2)
else:
    print(':(')
