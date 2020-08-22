n = int(input())
a = [int(input()) for i in range(n)]
b = sorted(a, reverse=True)
for i in a:
    if i == b[0]:
        print(b[1])
    else:
        print(b[0])
