n = int(input())
abcde = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    abcde[i][-1] *= 11/90
    ans = max(ans, sum(abcde[i]))
print(ans)
