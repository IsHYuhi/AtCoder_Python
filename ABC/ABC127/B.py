r, d, xi = map(int, input().split())

for i in range(1, 11):
    xi = r*xi - d
    print(xi)
