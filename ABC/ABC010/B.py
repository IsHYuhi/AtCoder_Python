n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    while i%3==2 or i%2==0:
        i -= 1
        ans += 1
print(ans)

