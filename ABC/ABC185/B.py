max_n, m, t = map(int, input().split())
n = max_n
ab = [list(map(int, input().split())) for _ in range(m)]
now = 0
for i in range(m):

    a, b = ab[i]
    n = min(max_n, n-(a-now))
    now = a
    if n<=0:
        print('No')
        exit()
    n = min(max_n, n+(b-now))
    now = b

if n-(t-now)<=0:

    print('No')
else:
    print('Yes')

