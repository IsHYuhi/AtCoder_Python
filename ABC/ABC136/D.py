import math
s = list(input())
count = [0]*len(s)

lc = 0
rc = 0
for i in range(len(s)-1):
    if s[i] == 'R':
        rc += 1
        if s[i+1] == 'L':
            count[i] += int(math.ceil(rc/2))
            count[i+1] += int(math.floor(rc/2))

            rc = 0

    elif s[i] == 'L':
        continue

count = count[::-1]
s = s[::-1]
lc = 0
rc = 0
for i in range(len(s)-1):
    if s[i] == 'L':
        lc += 1
        if s[i+1] == 'R' and rc == 0:
            count[i] += int(math.ceil(lc/2))
            count[i+1] += int(math.floor(lc/2))

            lc = 0

    elif s[i] == 'R':
        continue

print(' '.join(list(map(str, count[::-1]))))