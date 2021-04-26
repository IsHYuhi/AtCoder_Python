n = int(input())
s = input()
q = int(input())
tab = [list(map(int, input().split())) for _ in range(q)]

idxs_1 = [i for i in range(n)]
idxs_2 = [i for i in range(n, 2*n)]

for t, a, b in tab:
    if t == 1:
        if a<=n and n<b:
            idxs_1[a-1], idxs_2[b-1-n] = idxs_2[b-1-n], idxs_1[a-1]
        elif a<=n and b<=n:
            idxs_1[a-1], idxs_1[b-1] = idxs_1[b-1], idxs_1[a-1]
        elif n<a and n<b:
            idxs_2[a-1-n], idxs_2[b-1-n] = idxs_2[b-1-n], idxs_2[a-1-n]
    elif t == 2:
        idxs_1, idxs_2 = idxs_2, idxs_1


idxs = idxs_1 + idxs_2
print(''.join([s[i] for i in idxs]))