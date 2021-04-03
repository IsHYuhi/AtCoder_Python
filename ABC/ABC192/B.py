s = input()
s1 = s[::2]
s2 = s[1::2]
for i, l in enumerate(s, 1):

    if i%2==1 and (ord('a')<=ord(l)<=ord('z')):
        continue
    elif i%2==0 and (ord('A')<=ord(l)<=ord('Z')):
        continue
    else:
        print('No')
        exit()

print('Yes')
