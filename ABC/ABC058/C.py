from collections import Counter
n = int(input())
Si = [Counter(input()) for _ in range(n)]
letters = set(Si[0].keys())
for S in Si:
    letters = set(S.keys()) & letters
letters = list(letters)
letters.sort()
for key in letters:
    count = float('inf')
    for S in Si:
        count = min(count, S[key])
    print(key*count, end='')
print('')