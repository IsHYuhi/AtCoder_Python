import numpy as np
d = np.array(list(map(int, input().split())))
j = np.array(list(map(int, input().split())))

ans = np.sum(np.maximum(d, j))
print(ans)
