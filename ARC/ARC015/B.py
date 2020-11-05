n = int(input())
MmT = [list(map(float, input().split())) for _ in range(n)]
ans = [0]*6
for M, m in MmT:
    if M >= 35:
        ans[0] += 1
    elif M>= 30:
        ans[1] += 1
    elif M>=25:
        ans[2] += 1
    elif M<0:
        ans[5] += 1

    if m>=25:
        ans[3] += 1

    if m<0 and M>=0:
        ans[4] += 1

print(' '.join(list(map(str, ans))))