n = int(input())
a = map(int, input().split())
c = set(a)

if len(c) == n:
    print('YES')
else:
    print('NO')