n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i, v in enumerate(b):
    for j in range(2):
        m =  min(a[i+j], v)
        a [i+j] -= m
        v -= m
        ans += m
print(ans)
