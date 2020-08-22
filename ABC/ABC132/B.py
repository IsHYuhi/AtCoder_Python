n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, n-1):
    if (p[i] != max(p[i-1], p[i], p[i+1])) and (p[i] != min(p[i-1], p[i], p[i+1])):
        ans += 1
print(ans)
