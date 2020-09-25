n = int(input())
s = input()
for i in s:
    c = ord(i)+n
    if c >= 91:
        c = c-26
    print(chr(c), end='')
print()