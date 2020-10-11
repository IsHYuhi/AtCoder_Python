n = int(input())

def decomp(n):
    ans = float('inf')

    for i in range(1, int(-(-n**0.5//1))+1):
        if n%i == 0:
            ans = min(ans, max(len(str(i)), len(str(n//i))))
    print(ans)

decomp(n)