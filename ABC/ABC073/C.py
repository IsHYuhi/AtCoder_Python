from collections import Counter
n = int(input())
a = Counter([int(input()) for i in range(n)])
ans = 0
for num, c in a.items():
    if c%2==1:
        ans+=1
print(ans)
