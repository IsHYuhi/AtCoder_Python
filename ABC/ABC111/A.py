n = list(input())
ans = []
for i in n:
    if i=='9':
        ans.append('1')
    elif i=='1':
        ans.append('9')
    else:
        ans.append(i)
print(''.join(ans))
