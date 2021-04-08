s = input()

h = len(s)//2
s_inv = s[::-1][:h]
s = s[:h]

for i in range(h):
    if s[i] != s_inv[i] and s[i] != '*' and s_inv[i] != '*':
        print('NO')
        exit()

print('YES')
