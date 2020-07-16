c1 = input()
c2 = input()

if c1==c2[::-1] and c2==c1[::-1]:
    print('YES')
else:
    print('NO')