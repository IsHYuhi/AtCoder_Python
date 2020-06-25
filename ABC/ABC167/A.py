S = input()
T = input()

if S.islower() and T.islower() and 1<=len(S)<=10 and S == T[:-1]:
    print('Yes')
else:
    print('No')