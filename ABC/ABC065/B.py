n = int(input())
a = [int(input()) for _ in range(n)]
ans = 1
count = 0
while ans!=2:
    ans = a[ans-1]
    count += 1
    if count > len(a):
        print(-1)
        exit()
print(count)

