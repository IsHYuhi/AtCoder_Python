n = int(input())
A = list(map(int, input().split()))
if not sum(A)%n==0:
    print(-1)
    exit()

basic = sum(A)//n
ans = 0
for i in range(n-1):
    print(A[:i+1], A[i+1:],i+1, n-i-1, basic)
    if not (sum(A[:i+1]) == basic*(i+1) and sum(A[i+1:]) == basic*(n-i-1)):
        ans += 1
print(ans)