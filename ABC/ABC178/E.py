import numpy as np
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy = np.array([[i+j, i-j] for i, j in xy])

print(max(max(xy[:,0])-min(xy[:,0]), max(xy[:,1])-min(xy[:,1])))

