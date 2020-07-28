import math
nums = [int(input()) for _ in range(5)]
mn = float('inf')

for i in nums:
    if i%10!=0:
        mn = min(mn, i%10)
if mn == float('inf'):
    mn = 10

print(sum(list(map(lambda x: int(math.ceil(x/10)*10), nums)))-10+mn)
