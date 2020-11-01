n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for a, b in ab:
    ans += b*(b+1)//2 - a*(a-1)//2
print(ans)
