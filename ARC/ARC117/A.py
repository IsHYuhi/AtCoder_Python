a, b = map(int, input().split())

arrp = []
arrm = []
s = -1 if b>a else 1

for i in range(1, min(a, b)+1):
    arrp.append(i)
    arrm.append(-i)

for j in range(min(a, b)+1, a + b - min(a, b) + 1):
    if s == 1:
        arrp.append(s*j)
    else:
        arrm.append(s*j)

diff = abs(abs(sum(arrm))-abs(sum(arrp)))

i = 0
arrp.sort(reverse=True)
arrm.sort()
l = len(arrm) if s == 1 else len(arrp)

while i<diff:
    if s == 1:
        arrm[i%l] -= 1
    else:
        arrp[i%l] += 1
    i += 1

print(' '.join(list(map(str, arrp+arrm))))
