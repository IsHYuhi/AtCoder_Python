n = int(input())

cons = []
i = 1
d = 1
while i <= 50:
    for j in range(1, 10):
        cons.append(str(j)*d)
        i += 1
    d += 1

print(cons[n-1])
