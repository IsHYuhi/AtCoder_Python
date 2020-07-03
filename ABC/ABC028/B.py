from collections import Counter
S = list(input())
S = Counter(S)

abcdef = ['A', 'B', 'C', 'D', 'E', 'F']
for a in abcdef:
    if S.get(a):
        print(S[a], end='')
    else:
        print(0, end='')
    if a!='F':
        print(' ', end='')
print()