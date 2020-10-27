m, n, N = map(int, input().split())

def calc(S):
    ans = 0
    while S>=m:
        ans += (S//m)*n
        S = (S//m)*n + S%m
    return ans

print(calc(N)+N)