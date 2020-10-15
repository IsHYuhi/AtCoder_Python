n = int(input())
a = list(map(int, input().split()))
ans = -float('inf')

# if %2 == 1:
#     n -= 1

# for i in range(2, n, 2):
#     total = a[:i]
#     for j in range(i, n-i+1):

# ans = 0

for i in range(n):
    l_max = -float('inf')
    r_max = -float('inf')

    for j in range(n):
        if i==j:
            continue

        l_total = sum(a[min(i,j):max(i,j)+1:2])
        r_total = sum(a[min(i,j)+1:max(i,j)+1:2])

        if r_max < r_total:
            r_max = r_total
            l_max = l_total

    ans = max(ans, l_max)

print(ans)
