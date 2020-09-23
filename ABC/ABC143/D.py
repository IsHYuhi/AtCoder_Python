import bisect

n = int(input())
l = list(map(int, input().split()))

l.sort()
ans = 0
for i in range(n-1):
    b = l[:i]
    c = l[i+1:]
    for j in b:
        ans += bisect.bisect_left(c, l[i] + j)#2番目の棒より短く(left), 一定以上の長さを持つ([i+1:])
print(ans)
