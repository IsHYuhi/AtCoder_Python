n, l = map(int, input().split())
s = list(input())
count = 1
ans = 0
for h in s:
    if h == '+':
        count += 1
    elif h == '-' and count >= 1:
        count -= 1

    if count > l:
        count = 1
        ans += 1

print(ans)