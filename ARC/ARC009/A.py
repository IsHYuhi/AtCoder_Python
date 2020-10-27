n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in ab:
    ans += i[0]*i[1]
print(int(ans*1.05))