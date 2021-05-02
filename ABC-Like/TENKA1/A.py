from collections import Counter
s = list(input())

s = Counter(s)
if s.get('1'):
    print(s['1'])
else:
    print(0)
