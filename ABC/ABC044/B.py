from collections import Counter
s = input()
s = Counter(s)

for i in s.values():
    if i%2 != 0:
        print('No')
        exit()
print('Yes')