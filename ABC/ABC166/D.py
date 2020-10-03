x = int(input())
for i in range(-120,120):
    for j in range(-120,120):
        if i**5 - j**5 == x:
            print(i, j)
            exit()