n, a, b = map(int, input().split())

def comb(n, r):
    res = 1
    res_ = 1
    for i in range(n-r+1, n+1):
        res *= i
        res %= (10**9+7)
    for i in range(1, r+1):
        res_ *= pow(i, (10**9+7)-2, (10**9+7))
        res_ %= (10**9+7)
    #res_ = pow(res, (10**9+7)-2, (10**9+7))

    return res*res_

print((pow(2, n, (10**9+7)) -1 - comb(n, a) - comb(n, b)) % (10**9+7))

