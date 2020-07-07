n, l = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
ans = ''.join(s)
print(ans)