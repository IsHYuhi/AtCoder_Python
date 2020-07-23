from collections import Counter
n = int(input())
s = input()
ans = 0
for i in range(n-1):
    a, b = Counter(s[:i+1]), Counter(s[i+1:])
    inter = a.keys() & b.keys()
    ans = max(ans, len(inter))
print(ans)