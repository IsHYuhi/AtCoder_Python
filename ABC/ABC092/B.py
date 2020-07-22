n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0
for ai in a:
    ans += (d-1)//ai + 1

print(x+ans)