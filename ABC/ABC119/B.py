n = int(input())
xu = [list(input().split()) for _ in range(n)]
ans = 0
for x, u in xu:
    ans += float(x)*380000.0 if u=='BTC' else float(x)
print(ans)