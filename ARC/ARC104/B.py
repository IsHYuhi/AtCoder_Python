#AC with PyPy3
from collections import Counter
n, s = input().split()
n = int(n)

count_org = Counter(s)
count = 0

for i in range(1, n+1)[::-1]:
    count_t = count_org.copy()
    for j in range(i):

        if count_t['A'] == count_t['T'] and count_t['C'] == count_t['G']:
            count += 1

        count_t[s[j]] -= 1
    count_org[s[i-1]] -= 1

print(count)