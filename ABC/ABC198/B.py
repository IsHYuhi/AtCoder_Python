n = int(input())
strn = str(n)
count = 0

for i in strn[::-1]:
    if i == '0':
        count += 1
    else:
        break

strn = strn[:len(strn)-count]
if strn[:len(strn)//2] == strn[::-1][:len(strn)//2]:
    print('Yes')
else:
    print('No')
    