n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
m.sort()
ans = len(m)
x = x - sum(m)
ans += x//m[0]
print(ans)
