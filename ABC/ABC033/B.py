n = int(input())
s = []
r = []
for _ in range(n):
    _s, _r = input().split()
    s.append(_s)
    r.append(int(_r))
total = sum(r)//2

for i in range(n):
    if r[i]>total:
        print(s[i])
        exit()
print('atcoder')