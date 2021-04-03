import numpy as np
n, x = map(int, input().split())
a = list(map(int, input().split()))
a = [str(i) for i in a if i != x]

print(' '.join(a))