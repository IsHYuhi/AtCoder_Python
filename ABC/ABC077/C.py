from itertools import combinations
import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ans = 0

a_m = [0]*(n+1)
c_m = [0]*(n+1)

#biより真に小さいaiの数
i = 0
j = 0
while i<n:
    if j<n and a[j]<b[i]:
        a_m[i+1] += 1
        j +=1
    else:
        a_m[i+1] += a_m[i]
        i += 1

#biより真に大きいciの数
i = n-1
j = n-1
while i>=0:
    if b[i]<c[j] and j>=0:
        c_m[i] += 1
        j -= 1
    else:
        c_m[i] += c_m[i+1]
        i -= 1

a_m.pop(0)
c_m.pop()

for i in range(n):
    ans += a_m[i]*c_m[i]

print(ans)