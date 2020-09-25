import math
a, b = map(int, input().split())

print(int(a*b/math.gcd(a, b)))
