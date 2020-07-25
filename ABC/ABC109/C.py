import math
from functools import reduce

def gcd(numbers):
    return reduce(math.gcd, numbers)

n, x = map(int, input().split())
xn = list(map(int, input().split()))
xn = [abs(i-x) for i in xn]

print(gcd(xn))
