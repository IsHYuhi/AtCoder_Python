n, x = map(int, input().split())
s = list(input())
for i in s:
    if i == 'o':
        x += 1
    else:
        x = max(0, x-1)

print(x)