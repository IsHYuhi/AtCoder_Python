from collections import Counter
n = int(input())

a = list(map(int, input().split()))
counter = Counter(a)
l = n

ans = 0
a = a[:-1]
for i in a:
    ans += l-counter[i]
    counter[i] -= 1
    l -= 1
print(ans)