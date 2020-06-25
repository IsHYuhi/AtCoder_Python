#pypy
Sequence = [float('inf') for _ in range(1000000+1)]
Sequence[0] = 0
Sequence[1] = 0
Sequence[2] = 0
Sequence[3] = 1

def tribonacci(n):
    if Sequence[n] != float('inf'):
        return Sequence[n]
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

def tribonacci_h(n):
    if n == 1:
        return 0
    elif n ==2:
        return 0
    elif n ==3:
        return 1

    for i in range(4, n+1):
        Sequence[i] = (Sequence[i-3] + Sequence[i-2] + Sequence[i-1])%10007
    return Sequence[n]


n = int(input())
print(tribonacci_h(n)%10007)