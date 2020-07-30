n, k = map(int, input().split())
ans = 0

for i in range(1, n+1):
    if i<k:
        for j in range(1, 18):
            if i*(2**j) >= k:
                e = j
                break
    else:
        e = 0

    ans += (1/n)*(2**(-e))

print(ans)
