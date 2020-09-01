from collections import Counter

n = int(input())
c = list(input())
count = Counter(c)
ans = float('inf')
w = 0
r = 0

if count.get('R'):
    r = count['R']

ans = max(w, r)

for i in range(n):
    if c[i]=='W':
        w += 1
    else:
        r -= 1
    ans =min(max(w,r), ans)
print(ans)