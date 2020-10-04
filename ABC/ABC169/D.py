import bisect
def factorization(n):
    if n == 1:
        return []
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n = int(input())

sigma = [1]
for i in range(2, 20):
    sigma.append(i+sigma[i-2])
ans = 0
for i, j in factorization(n):
    ans += bisect.bisect_right(sigma, j)

print(ans)