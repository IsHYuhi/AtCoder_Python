from bisect import bisect
k, s = map(int, input().split())
ans = 0
rekkyo = []
for i in range(0,k+1):
    for j in range(0,k+1):
        if 0<=s-i-j<=k:
            ans+=1
print(ans)
