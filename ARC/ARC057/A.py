a, k = map(int, input().split())

i = 0
an = a

if k == 0:
    print(int(2*1e12-a))
    exit()

while an<2*1e12:
    an += k*an + 1
    i += 1
print(i)