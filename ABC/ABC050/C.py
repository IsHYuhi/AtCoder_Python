from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
d = list(c.values())
if (n % 2 == 1 and c[0] == 1 and d.count(2) == (n-1)//2) or (n % 2 == 0 and d.count(2) == n//2):
    print((2**(n//2)) % (10**9+7))
else:
    print(0)