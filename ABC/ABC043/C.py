import numpy as np
n = int(input())
a = np.asarray(list(map(int, input().split())))
m = float('inf')

for i in range(-100, 101):
    m = min(np.sum((a-i)**2), m)
print(m)
