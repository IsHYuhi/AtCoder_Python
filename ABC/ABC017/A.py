ans = 0
for i in range(3):
    s, e = map(int, input().split())
    ans += int(s*e/10)
print(ans)
