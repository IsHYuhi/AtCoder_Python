x = input()
s = input()

s = [i for i in s if i != x]
print(''.join(s))