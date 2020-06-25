import math
N = int(input())
A = list(map(int, input().split()))

print(math.ceil(sum(A)/(N-A.count(0))))