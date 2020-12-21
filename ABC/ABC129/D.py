#AC with PyPy3, TLE with Python3

#import numpy as np
h, w = map(int, input().split())
field = [input() for _ in range(h)]
acc_field = [[0]*w for _ in range(h)]
ans = 0
for i in range(h):
    to_right = [0]*w
    to_left = [0]*w
    to_right[0] = 1 if field[i][0] == '.' else 0
    to_left[w-1] = 1 if field[i][w-1] == '.' else 0

    for j in range(1, w):
        to_right[j] = to_right[j-1] + 1 if field[i][j] == '.' else 0
        to_left[w-j-1] = to_left[w-j] + 1 if field[i][w-j-1] == '.' else 0

    for j in range(w):
        acc_field[i][j] = max(0, to_right[j]+to_left[j]-1)

for j in range(w):
    to_lower = [0]*h
    to_upper = [0]*h
    to_lower[0] = 1 if field[0][j] == '.' else 0
    to_upper[h-1] = 1 if field[h-1][j] == '.' else 0

    for i in range(1, h):
        to_lower[i] = to_lower[i-1] + 1 if field[i][j] == '.' else 0
        to_upper[h-i-1] = to_upper[h-i] + 1 if field[h-i-1][j] == '.' else 0

    for i in range(h):
        acc_field[i][j] += max(0, to_lower[i]+to_upper[i]-1)
        ans = max(ans, acc_field[i][j]-1)

print(ans)
#print(max(0, np.max(acc_field)-1))

