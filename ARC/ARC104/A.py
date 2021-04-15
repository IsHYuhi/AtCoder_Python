a, b = map(int, input().split())

for i in range(-100, 101):
    for j in range(-100, 101):
        if i+j == a and i-j == b:
            print(i, j)
            exit()