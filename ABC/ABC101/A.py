s = list(input())
ans = 0
for i in s:
    if i=='+':
        ans += 1
    else:
        ans -= 1
print(ans)