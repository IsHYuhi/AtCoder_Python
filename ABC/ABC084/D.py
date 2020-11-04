import numpy as np

def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

q = int(input())
lr =[]
MAX = 0
for i in range(q):
    l, r = map(int, input().split())
    lr.append([l, r])
    MAX = max(MAX, r)

primes = seachPrimeNum(int(MAX))
l = len(primes)
dic = {}

for i in primes:
    dic[i] = True

co_primes = []
for i in range(l):
    if dic.get((primes[i]+1)//2):
        co_primes.append(primes[i])

prime_for_lr = []
max_l = len(co_primes)
now = 0

for i in range(MAX+1):
    if now >= max_l:
        prime_for_lr.append(now)

    elif i<co_primes[now]:
        prime_for_lr.append(now)

    else:
        now += 1
        prime_for_lr.append(now)

for l, r in lr:
    print(prime_for_lr[r]-prime_for_lr[l-1])
