import math
a, b = input().split()
ab = int(a+b)
for i in range(1,1001):
    if i**2==ab:
        print('Yes')
        exit()
print('No')
