N = int(input())
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

sum = 0
for a in range(1,N+1):
    for b in range(1,N+1):
        for c in range(1,N+1):
            sum += gcd(a, b, c)
print(sum)