n = int(input())

field = [list(input()) for _ in range(n)]
for i in range(n):
    for j in reversed(range(n)):
        print(field[j][i], end='')
    print('')