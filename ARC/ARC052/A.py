s = input()
num = [i for i in s if ord('0')<=ord(i)<=ord('9')]
print(''.join(num))