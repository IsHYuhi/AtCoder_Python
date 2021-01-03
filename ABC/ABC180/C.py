import math
n = int(input())

def decomp(n):
    ans = []
    ans_ = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            ans.append(i)
            if n//i != i:
                ans_.append(n//i)
            #if (n//i)*i==n:
    return ans+ans_[::-1]

ans = decomp(n)
for i in ans:
    print(i)
