n, m, a, b = map(int, input().split())
c = [int(input()) for _ in range(m)]

for day, i in enumerate(c, 1):
    if n<=a:
        n += b
    n -= i
    if n < 0:
        print(day)
        exit()

print('complete')