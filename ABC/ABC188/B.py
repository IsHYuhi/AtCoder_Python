import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

if not np.sum(a*b):
    print('Yes')
else:
    print('No')
