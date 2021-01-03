import math
n = int(input())
x = list(map(lambda x: abs(int(x)), input().split()))
print(sum(x))
mx = max(x)
x = [i**2 for i in x]
print(math.sqrt(sum(x)))
print(mx)