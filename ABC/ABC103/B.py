s = input()
t = input()

for i in range(len(s)):
    if t == s[i:]+s[:i]:
        print('Yes')
        exit()
print('No')