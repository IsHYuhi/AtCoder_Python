s = list(input())

one = 0
zero = 0

for i in s[::2]:
    if i == '1':
        one += 1
    else:
        zero += 1

for i in s[1::2]:
    if i == '0':
        one += 1
    else:
        zero += 1

print(min(one, zero))