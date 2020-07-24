import math
n, k = map(int, input().split())
an = list(map(int, input().split()))
n = n-k
ans = math.ceil(n/(k-1)) + 1
print(ans)