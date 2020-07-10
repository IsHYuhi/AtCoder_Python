a, b, c = map(int, input().split())

for i in range(b+1):
    if a*i%b==c:
        print('YES')
        exit()
print('NO')