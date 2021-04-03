from collections import Counter
s = Counter(list(input()))
if len(s)==1:
    print('Won')
else:
    print('Lost')
