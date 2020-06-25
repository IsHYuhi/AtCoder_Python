import re
rep = set(['a', 't', 'c', 'o', 'd', 'e', 'r'])
S = list(input())
T = list(input())

# S = re.sub('@', '.', S)
# T = re.sub('@', '.', T)
#print(S)
for i, st in enumerate(zip(S, T)):
    if st[0]=='@' and st[1] in rep:
        T[i] = '@'
    elif st[1]=='@' and st[0] in rep:
        S[i] = '@'
# S = str(S)
# T = str(T)
# print(S)
# print(T)
if S==T:
    print('You can win')
else:
    print('You will lose')
#print(re.fullmatch(S, T))