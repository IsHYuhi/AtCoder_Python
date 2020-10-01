from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
ans = 0
for key, value in b.items():
    ans += (value*(value-1))//2

for i in range(n):
    print(ans - b[a[i]] +1)
