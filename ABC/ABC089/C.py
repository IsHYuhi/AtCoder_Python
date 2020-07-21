from collections import Counter
import itertools

n = int(input())
s = [input()[:1] for _ in range(n)]
s = Counter([i for i in s if i in ['M', 'A', 'R', 'C', 'H']])

li = list(itertools.combinations(['M', 'A', 'R', 'C', 'H'], 3))

if len(s)<3:
    print(0)
    exit()

ans = 0
for i, j, k in li:
    ans += s[i]*s[j]*s[k]
print(ans)