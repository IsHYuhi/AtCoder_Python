import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
an = list(map(int, input().split()))
l = lcm(an)-1
an = [l%i for i in an]
print(sum(an))