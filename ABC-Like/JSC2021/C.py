a, b = map(int, input().split())

ans = 1
for i in range(1, b+1):
    if a <= (b//i)*i <= b and a <= (b//i)*(i-1) <= b:
        ans = max(ans, b//i)
print(ans)