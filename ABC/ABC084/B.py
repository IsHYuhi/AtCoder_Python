a, b = map(int, input().split())
s = input().split('-')
if len(s)!=2:
    print('No')
    exit()

if a==len(s[0]) and b==len(s[1]):
    print('Yes')
else:
    print('No')
