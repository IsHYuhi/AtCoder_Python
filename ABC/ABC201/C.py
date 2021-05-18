s = list(input())
ok = []
no = []
for i in range(10):
    if s[i] == 'o':
        ok.append(str(i))
    elif s[i] == 'x':
        no.append(str(i))

ans = 0
for i in range(10000):
    flag = 1
    now = list(str(i).zfill(4))

    for j in ok:
        if j not in now:
            flag = 0
    for j in no:
        if j in now:
            flag = 0

    if flag == 1:
        ans += 1

print(ans)