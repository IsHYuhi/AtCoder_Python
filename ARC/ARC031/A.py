name = input()
if name[:len(name)//2] == name[::-1][:len(name)//2]:
    print('YES')
else:
    print('NO')