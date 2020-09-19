ans = 0
n = int(input())
for a in range(1, n):
    for b in range(a, n):
        if a*b>=n:
            break
        if a==b:
            ans+=1
        else:
            ans += 2
print(ans)