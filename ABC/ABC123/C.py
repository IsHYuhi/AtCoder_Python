import math
n = int(input())
nums = [int(input()) for _ in range(5)]
mn = min(nums)

print(4+math.ceil(n/mn))