n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))

s = set()
s.add(a)
for i in p:
    if i not in s:
        s.add(i)
    else:
        print('NO')
        exit()

if b in s:
    print('NO')
else:
    print('YES')