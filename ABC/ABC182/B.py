n = int(input())
a = list(map(int, input().split()))
mx = max(a)
ans = 0
max_count = 0
for i in range(2, mx+1):
    count = 0
    for j in a:
        if j % i == 0:
            count += 1

    if count > max_count:
        ans = i
        max_count = count

print(ans)
