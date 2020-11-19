n = int(input())
s =[list(input()) for _ in range(2)]
mod = 10**9 + 7
if s[0][0] == s[1][0]:
    start = 1
    ans = 3
else:
    start = 2
    ans = 6

i = start
while i < n:
    #check this position
    if s[0][i]==s[1][i]:
        v = 1
        j = 1
    else:
        v = 0
        j = 2

    #check left
    if s[0][i-1] == s[1][i-1]:
        lv = 1
    else:
        lv = 0

    if v == 1 and lv == 1:
        ans *= 2
    if v == 1 and lv == 0:
        ans *= 1
    if v == 0 and lv == 1:
        ans *= 2
    if v == 0 and lv == 0:
        ans *= 3

    ans %= mod
    i += j

print(ans)
