a, b = map(int, input().split())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp%i==0:
            arr.append(i)
            while temp%i==0:
                temp //= i

    if temp>1:
        arr.append(temp)

    return arr

a_prime = factorization(a)
b_prime = factorization(b)
count = 0
for i in a_prime:
    if i in b_prime:
        count += 1
print(count+1)
