n, k = map(str, input().split())
k = int(''.join(k))

def g1(x):
    return int(''.join(sorted(x, reverse=True)))

def g2(x):
    return int(''.join(sorted(x)))

next = str(n)
for i in range(k):
    next = list(str(g1(next)-g2(next)))

print(''.join(next))