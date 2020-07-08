s, c = map(int, input().split())
ans = 0
ans += min(s,c//2)
res = c-min(s,c//2)*2
ans += res//4
print(ans)