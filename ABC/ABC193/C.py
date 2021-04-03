n = int(input())
expressed = set()

for i in range(2, int(n**0.5)+1):
    k = i*i
    while k <= n:
        expressed.add(k)
        k *= i

print(n-len(expressed))