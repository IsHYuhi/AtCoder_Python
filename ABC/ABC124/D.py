n, k = map(int, input().split())
s = list(map(int, list(input())))
comp = []

c = 1
p = s[0]
for i in range(1, n):
    if s[i] == p:
        c += 1

    else:
        comp.append([s[i-1], c])
        c = 1
        p = s[i]

comp.append([s[n-1], c])

l = len(comp)
count = 0
d = 0
sum_ = 0
ans = []
while d<l:
    if comp[d][0]==1 and count==k:
        sum_ += comp[d][1]
        break

    elif comp[d][0]==0:
        count += 1
    sum_ += comp[d][1]
    d+=1

ans.append(sum_)
for j in range(d+1, l, 2):
    if j<l:#明示
        sum_ += comp[j][1]

    if j+1<l:
        sum_ += comp[j+1][1]

    if j-k*2-1>=0:
        sum_ -= comp[j-k*2-1][1]

    if j-k*2>=0:
        sum_ -= comp[j-k*2][1]

    ans.append(sum_)

if not ans:
    print(n)
else:
    print(max(ans))
