import numpy as np
n = int(input())
matrix_C = np.array([list(map(int, input().split())) for _ in range(n)])

a1 = np.min(matrix_C[:, 0])
b1 = matrix_C[0][0]-a1
a = [j-b1 for j in matrix_C[0]]
b = [j-a1 for j in matrix_C[:, 0]]

ans = []
for i in range(n):
    ans.append(np.array(a)+b[i])

if (np.array(ans)==(matrix_C)).all() == True:
    print('Yes')
    print(' '.join(map(str, b)))
    print(' '.join(map(str, a)))
else:
    print('No')

