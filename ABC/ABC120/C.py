from collections import Counter
s = list(input())
s = Counter(s)
print(min(s['0'], s['1']) * 2)
