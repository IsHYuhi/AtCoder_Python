import math

def min_prime(start, limit):
    for k in range(start, limit+1):

        if k%2 == 0 and k !=2:
            continue

        factor = 0

        for divisor in range(2, math.ceil(math.sqrt(k))):
            if k % divisor == 0:
                factor += 1

        if factor == 0:
            return k

x = int(input())
print(min_prime(x, 10**6))
