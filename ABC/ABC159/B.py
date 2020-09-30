S = input()
N = len(S)

if (S == S[::-1]) and (S[0:int((N-1)/2)]==S[int((N-1)/2-1)::-1]) and (S[int((N+3)/2-1):N]==S[:int((N+3)/2-2):-1]):
    print('Yes')
else:
    print('No')