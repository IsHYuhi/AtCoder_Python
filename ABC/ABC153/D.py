import math

h = int(input())
count = 0
e = 0
while h>0:
    count += 1*2**e
    e += 1
    if h == 1:
        h =0
    else:
        h = int(math.floor(h/2))
print(count)