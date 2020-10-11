s = input()
t = ''

idx = 0
fi = ['dream', 'erase']
si = 'eraser'
se = 'dreamer'

while idx < len(s):

    if s[idx:idx+6]==si and ((idx+9<len(s) and s[idx+6:idx+9] != 'ase') or idx+6==len(s)):
        idx += 6

    elif s[idx:idx+7]==se and ((idx+10<len(s) and s[idx+7:idx+10] != 'ase') or idx+7==len(s)):
        idx += 7

    elif s[idx:idx+5] in fi:
        idx += 5

    else:
        print('NO')
        exit()

    if idx == len(s):
        print('YES')
        exit()

print('NO')