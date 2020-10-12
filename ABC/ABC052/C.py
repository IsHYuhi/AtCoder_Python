import math

def factorization(n):
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

ex = [1]*1001
ans = 1

for i in range(2, n+1):
    n_fact = factorization(i)
    for j, k in n_fact:
        ex[j] += k

for i in ex:
    ans *= i
    ans %= (10**9+7)
print(ans)