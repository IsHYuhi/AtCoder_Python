n = int(input())

def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False

    return True

if n==1:
    print('Not Prime')
    exit()

if ( str(n)[-1]!='5' and (n%10)%2!=0 and sum(list(map(int, list(str(n)))))%3 != 0 ) or is_prime(n):
    print('Prime')
else:
    print('Not Prime')