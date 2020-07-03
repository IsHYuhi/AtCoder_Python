import math
N = int(input())
R = []
for i in range(N):
    R.append(int(input()))
R.sort(reverse=True)
ans = 0
for i, r in enumerate(R):
    if i%2==0:
        ans += r*r*math.pi
    else:
        ans -= r*r*math.pi
print(ans)
