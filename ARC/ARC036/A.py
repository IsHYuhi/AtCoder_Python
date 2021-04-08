n, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
for i in range(n-2):
    if sum(t[i:i+3]) < k:
        print(i+3)
        exit()
print(-1)