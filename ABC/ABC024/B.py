N, T = map(int, input().split())
A = []
for i in range(N):
    a = int(input())
    A.append(a)
ans = 0
for i in range(N-1):
    if A[i]+T<=A[i+1]:
        ans += T
    else:
        ans += (A[i+1]-A[i])
print(ans+T)
