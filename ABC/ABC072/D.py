n = int(input())
p = list(map(int, input().split()))
i=0
ans =0
while i<n-1:
    if p[i]==i+1:
        p[i], p[i+1] = p[i+1], p[i]
        ans += 1
    i+=1
if p[n-1]==n:
    ans+=1
print(ans)
