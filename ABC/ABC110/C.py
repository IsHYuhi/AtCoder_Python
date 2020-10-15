s = input()
t = input()

s_count = dict()
t_count = dict()

for i in range(26):
    s_count[chr(ord('a')+i)] = []
    t_count[chr(ord('a')+i)] = []

for i in range(len(s)):
    s_count[s[i]].append(i)
    t_count[t[i]].append(i)

s = sorted(set(s), key=s.index)
print(s)
t = sorted(set(t), key=t.index)
print(t)

for i in range(len(s)):
    if s_count[s[i]]!=t_count[t[i]]:
        print('No')
        exit()

print('Yes')