K = int(input())
S = input()

if len(S)<=K:
    print(S)
else:
    S = S[:K]+'...'
    print(S)