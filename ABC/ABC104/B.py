from collections import Counter
s = list(input())
n = len(s)
count = Counter(s[2:-1])
lower = [i for i in s if ord('a')<=ord(i)<=ord('z')]

if count.get('C'):
    if count['C']==1 and s[0]=='A' and len(lower)==n-2:
        print('AC')
        exit()
print('WA')