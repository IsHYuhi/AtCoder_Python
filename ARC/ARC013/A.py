from itertools import permutations

n, m, l = map(int, input().split())
pqr = list(map(int, input().split()))
ans = 0
idx = [i for i in range(3)]
idx = permutations(idx, 3)

for pi, qi, ri in idx:
    ans = max((n//pqr[pi])*(m//pqr[qi])*(l//pqr[ri]), ans)

print(ans)
