n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in x:
    ans += min(abs(i-0), abs(i-k))
print(ans*2)