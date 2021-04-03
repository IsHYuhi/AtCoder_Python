n, s, d = map(int, input().split())

ans = 'No'
for _ in range(n):
    x, y = map(int, input().split())
    if x<s and y>d:
        ans = 'Yes'
print(ans)