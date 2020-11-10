n = int(input())
a = list(map(int, input().split()))
ra = sorted(a, reverse=True)
ans = [0]*n
for i in range(n)[::-1]:
    s = sum(ans[i::i+1])%2
    if s!=a[i]:
        ans[i] = 1
    else:
        ans[i] = 0


print(sum(ans))

idxs = [idx for idx, v in enumerate(ans, 1) if v == 1]
if idxs:
    print(' '.join(list(map(str, idxs))))
