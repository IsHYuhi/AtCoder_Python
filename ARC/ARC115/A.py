from collections import deque
n, m = map(int, input().split())
s = [input() for _ in range(n)]

def check(str1, str2):
    count1 = 0
    count0 = 0
    for i, j in zip(str1, str2):
        if i!=j:
            if i == '1':
                count1 += 1
            else:
                count0 += 1
    if count1==count0 or (count1+count0)%2==0:
        return 1
    else:
        return 0

s = deque(s)
count = 0
off = 1
c = s[0]
idx = []
c = s.popleft()
l = len(s)
ite = 0

while s:
    if ite == l:
        c = s.popleft()
        l = len(s)
        off = 1

    ite += 1

    if not s:
        break

    nex = s.popleft()
    if check(c, nex) == 1:
        c = nex
        count += off
        off += 1
    else:
        s.append(nex)

total = n*(n-1)//2
print(total - count)