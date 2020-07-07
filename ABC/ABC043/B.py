s = input()
ans = []

for i in s:
    if i=='0':
        ans.append('0')
    elif i=='1':
        ans.append('1')
    elif i=='B' and ans:
        ans.pop()
print(''.join(ans))