l, h = map(int, input().split())
n = int(input())
times = [int(input()) for _ in range(n)]
for t in times:
    if t <= l:
        print(l-t)
    elif l <= t <= h:
        print(0)
    elif h <= t:
        print(-1)