A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

discount = 0
if S+T>=K:
    discount = -(S+T)*C
print(A*S+B*T+discount)