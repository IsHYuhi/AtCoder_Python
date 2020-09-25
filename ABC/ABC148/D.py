n = int(input())
a = list(map(int, input().split()))
c = 1
for j in a:
    if j==c:
        c += 1

if c==1:
    print(-1)
else:
    print(n-c+1)
