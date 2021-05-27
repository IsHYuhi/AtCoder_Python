a, b, k = map(int, input().split())
fac = [1]*(a+b+1)
for i in range(1, a+b+1):
    fac[i] = i*fac[i-1]

ans = ''
while True:

    if a == 0:
        ans += 'b'*b
        break
    elif b == 0:
        ans += 'a'*a
        break

    if k <= fac[a-1+b]//(fac[a-1]*fac[b]):
        ans += 'a'
        a -= 1

    else:
        ans += 'b'
        k -= fac[a-1+b]//(fac[a-1]*fac[b])
        b -= 1

print(ans)