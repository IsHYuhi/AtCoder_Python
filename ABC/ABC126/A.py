n, k = map(int, input().split())
s = input()
for i in range(n):
    if i==k-1:
        print(s[i].lower(), end='')
    else:
        print(s[i], end='')
print()
