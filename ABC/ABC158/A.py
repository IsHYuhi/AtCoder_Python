from collections import Counter
s = input()
s = Counter(s)
if len(s)==1:
    print('No')
else:
    print('Yes')