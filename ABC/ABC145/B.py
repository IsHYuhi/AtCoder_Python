n = int(input())
s = input()

if len(s)%2==0 and s[:len(s)//2]==s[len(s)//2:]:
    print('Yes')
else:
    print('No')