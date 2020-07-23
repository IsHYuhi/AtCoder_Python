x = int(input())
ans = 0
for b in range(1, 33):
    for p in range(2, 12):
        if b**p<=x:
            ans = max(ans, b**p)
print(ans)
