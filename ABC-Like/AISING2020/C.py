from itertools import product
n = int(input())
base = [i for i in range(1, int(n**0.5)+1)]
comb = list(product(base, repeat=3))

ans = dict()
for x, y, z in comb:
    if ans.get(x**2 + y**2 + z**2 + x*y + y*z + z*x) :
        ans[x**2 + y**2 + z**2 + x*y + y*z + z*x] += 1
    else:
        ans[x**2 + y**2 + z**2 + x*y + y*z + z*x] = 1

for i in range(1, n+1):
    if ans.get(i):
        print(ans[i])
    else:
        print(0)