n = int(input())
b = list(map(int, input().split()))
ans = b[0]
p = b[0]
for i in b[1:]:
    ans += min(p, i)
    p = i
ans += b[-1]
print(ans)