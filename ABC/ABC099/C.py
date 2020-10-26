import math
n = int(input())

def check(n, a):
    count = 0
    o = a*n
    start = n

    while start<=o:
        start *= n
    start //= n

    while start > 1:
        if o >= start:
            c = o//start
            o -= c*start
            count += c
        start //= n

    return count


ans = float('inf')
for nine_p in range(n//9+1):
    res_9 = n-9*nine_p
    six_p = res_9//6
    res = res_9 - six_p*6

    ans = min(check(9,nine_p)+check(6, six_p)+res, ans)

print(ans)
