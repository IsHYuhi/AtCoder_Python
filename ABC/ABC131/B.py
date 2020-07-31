n, l = map(int, input().split())
apples = [l+i-1 for i in range(1, n+1)]
mn = float('inf')
idx = 0
for i in range(n):
    if mn>abs(apples[i]):
        mn = abs(apples[i])
        idx = i

print(sum(apples)-apples[idx])
