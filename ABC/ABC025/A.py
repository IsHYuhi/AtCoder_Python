import itertools
S = list(input())
N = int(input())
lis = []
S = sorted(S)
i = (N-1)//5
j = (N-1)%5
print(S[i]+S[j])

