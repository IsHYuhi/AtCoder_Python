from collections import Counter
n = int(input())
s = input()
sn = Counter(s)

#リーダーよりwest側でwest方向をむいている人
l = 0
#リーダーよりeast側でeast方向をむいている人
r = sn['E']

#リーダーに一番west側の人を選んだときからスタート
ans = r
for i in range(n):
    if s[i] == 'W':
        l += 1
    else:
        r -= 1
    ans = min(ans, l+r)
print(ans)
