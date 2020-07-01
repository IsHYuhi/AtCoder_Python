S = input()

i = 0
while i<len(S):
    if S[i]=='o' or S[i] == 'k' or S[i] == 'u':
        i+=1
    elif S[i:i+2]=='ch':
        i+=2
    else:
        break
if len(S)==i:
    print('YES')
else:
    print('NO')