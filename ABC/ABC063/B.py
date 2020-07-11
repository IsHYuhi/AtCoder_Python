from collections import Counter
S = input()
Sd = Counter(S)

if len(Sd)==len(S):
    print('yes')
else:
    print('no')