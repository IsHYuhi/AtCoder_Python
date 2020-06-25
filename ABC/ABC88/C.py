C = [list(map(int, input().split())) for i in range(3)]
a1 = 0
b1 = C[0][0] - a1
b2 = C[0][1] - a1
b3 = C[0][2] - a1
a2 = C[1][1] - b2
a3 = C[2][2] - b3
As = [a1, a2, a3]
Bs = [b1, b2, b3]
for i in range(3):
    for j in range(3):
        if C[i][j] != As[i] + Bs[j]:
            print("No")
            exit()
print("Yes")