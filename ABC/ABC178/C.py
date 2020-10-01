import math
p  = 10**9+7
n = int(input())

print(((10**n)%p-(9**n)%p-(9**n)%p+(8**n)%p)%p)