def fun(N, K):
    if N%K > K:
        return K
    return fun(K, N%K)

N, K= list(map(int, input().split()))
if N%K == 0:
    print(0)
    exit()
N = N%K
while N>abs(N-K):
    N = abs(N-K)
print(N)
