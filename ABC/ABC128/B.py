n = int(input())

sp = []
for i in range(n):
    _s, _p = input().split()
    sp.append((_s, int(_p), i+1))

sp.sort(reverse=True, key=lambda x:x[1])
sp.sort(key=lambda x:x[0])

for i in sp:
    print(i[2])
