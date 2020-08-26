s = list(input())

for i in s[::2]:
    if i=='L':
        print('No')
        exit()

for i in s[1::2]:
    if i=='R':
        print('No')
        exit()

print('Yes')