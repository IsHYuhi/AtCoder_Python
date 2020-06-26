def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N = int(input())
N = 2025-N
div = make_divisors(N)
for i in range(len(div)):
    if div[len(div)-1-i] <= 9 and div[i] <= 9:
        print(str(div[i])+' x '+str(div[len(div)-1-i]))
