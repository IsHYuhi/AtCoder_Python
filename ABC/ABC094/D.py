n = int(input())
a = list(map(int, input().split()))

max_n = max(a)

if max_n%2 == 0:
    tmp_r = max_n//2#軸
    if tmp_r in a:
        print(max_n, tmp_r)
        exit()
else:
    tmp_r = max_n//2#対象

a.sort()
a_lower = []
a_upper = []
for i in range(n-1):#comb(aj, ai), aj>ai
    if a[i]<tmp_r:
        a_lower.append(a[i])
    else:
        a_upper.append(a[i])

if not a_upper:
    print(max_n, a_lower[-1])
    exit()

if abs(tmp_r-a_lower[-1]) <= abs(tmp_r+1-a_upper[0]):
    print(max_n, a_lower[-1])
else:
    print(max_n, a_upper[0])
