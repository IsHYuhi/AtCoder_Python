s = input().split()
ans = []
for p in s:
    if p == 'Left':
        ans.append('<')
    elif p == 'Right':
        ans.append('>')
    else:
        ans.append('A')

print(' '.join(ans))
