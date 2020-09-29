n = int(input())
s = list(input())
p = s[0]
ans = 1
for i in s[1:]:
    if p!=i:
        p = i
        ans += 1
print(ans)
