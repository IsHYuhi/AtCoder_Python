from functools import reduce
import math
import numpy as np
from itertools import combinations
n = int(input())
x = list(map(int, input().split()))

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

p = primes(50)
l = len(x)
ans = []
for i in range(2, l+1):
    ans.extend(list(map(np.prod, combinations(p, i))))
ans.extend(p)

for i in ans:
    flag = 0
    for j in x:
        if math.gcd(i, j) == 1:
            flag = 1
            break
    if flag == 0:
        print(i)
        exit()
