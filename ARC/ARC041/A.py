x, y = map(int, input().split())
k = int(input())

print(x + min(y, k) + min(0, y-k))