import math

def main():
    mod = 10**9+7
    n, k = map(int, input().split())
    ans = 0
    p = [0]*(n+1)
    pr = [0]*(n+1)
    pr[0] = n
    for i in range(1, n+1):
        p[i] = i+p[i-1]
        pr[i] = (n-i)+pr[i-1]

    for i in range(k, n+2):
        ans += pr[i-1]-p[i-1]+1
        ans %= mod
    print(ans%mod)

if __name__ == '__main__':
    main()