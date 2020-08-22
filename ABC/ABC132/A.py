from collections import Counter
S = list(input())
S = Counter(S)

if len(S)==2:
    for i, j in S.items():
        if j != 2:
            print('No')
            exit()

    print('Yes')
else:
    print('No')
