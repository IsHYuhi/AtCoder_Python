#PyPy3
n = int(input())
ans = 1
for i in range(1,n+1):
    ans = (ans*i)%1000000007
print(ans)