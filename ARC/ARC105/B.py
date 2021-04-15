from functools import reduce
import math

def my_gcd(numbers):
    return reduce(math.gcd, numbers)

n = int(input())
a = list(map(int, input().split()))
print(my_gcd(a))