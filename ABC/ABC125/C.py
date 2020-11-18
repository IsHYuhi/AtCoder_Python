import math
from functools import reduce
n = int(input())
a = list(map(int, input().split()))

def gcd_list(numbers):
    if not numbers:
        return 0
    return reduce(math.gcd, numbers)

lefts = [0]*(n)
rights = [0]*(n)

for i in range(1, n):
    lefts[i] = math.gcd(lefts[i-1], a[i-1])
    rights[i] = math.gcd(rights[i-1], a[n-i])

max_ = 0
for i in range(n):
    left = lefts[i]
    right = rights[n-i-1]
    max_ = max(math.gcd(left, right), max_)

print(max_)
