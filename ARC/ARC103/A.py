from collections import Counter
n = int(input())
v = list(map(int, input().split()))

v1_c = Counter(v[::2])
v2_c = Counter(v[1::2])
v1_c = sorted(list(v1_c.items()), key=lambda x: x[1])
v2_c = sorted(list(v2_c.items()), key=lambda x: x[1])

v1 = v1_c
v2 = v2_c

ans_1 = 0

if v1[-1][0]==v2[-1][0]:
    ans_1 += v1[-1][1]
    v1 = v1[:-1]

if len(v1)>=2:
    for i, j in v1[:-1]:
        ans_1 += j

if len(v2)>=2:
    for i, j in v2[:-1]:
        ans_1 += j

v1 = v1_c
v2 = v2_c

ans_2 = 0

if v1[-1][0]==v2[-1][0]:
    ans_2 += v2[-1][1]
    v2 = v2[:-1]

if len(v2)>=2:
    for i, j in v2[:-1]:
        ans_2 += j

if len(v1)>=2:
    for i, j in v1[:-1]:
        ans_2 += j

print(min(ans_1, ans_2))