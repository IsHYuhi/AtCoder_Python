n, k = map(int, input().split())

ans = 0
count = 0
div_count = 0
for i in range(1, n+1):
    if i%k == 0:
        count += 1

    if k%2 == 0:
        if i%k == k//2:
            div_count += 1

print(count**3 + div_count**3)
