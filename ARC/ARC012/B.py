n, va, vb, l = map(int, input().split())

for i in range(n):
    s = l/va
    l = vb*s
    if 10e-7 >= l:
        l = 0
print(l)