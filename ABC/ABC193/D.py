from collections import Counter

k = int(input())
s = list(input())
t = list(input())
st = s+t
sc = Counter(s)
tc = Counter(t)
total = Counter(st)
s_score = 0
t_score = 0

total = Counter(st)


for i in range(1, 10):
    if sc.get(str(i)):
        s_score += i*(10**sc[str(i)])
    else:
        s_score += i

    if tc.get(str(i)):
        t_score += i*(10**tc[str(i)])
    else:
        t_score += i

count = {}
for i in range(1, 10):
    if not total.get(str(i)):
        count[str(i)] = k
    else:
        count[str(i)] = k - total[str(i)]

ans_u = 0
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        tmp_s_score = s_score
        if sc.get(str(i)):
            tmp_s_score += -i*(10**sc[str(i)]) + i*(10**(sc[str(i)]+1))
        else:
            tmp_s_score += -i + i*10

        tmp_t_score = t_score
        if tc.get(str(j)):
            tmp_t_score += -j*(10**tc[str(j)]) + j*(10**(tc[str(j)]+1))
        else:
            tmp_t_score += -j + j*10

        if i==j:
            ans += count[str(i)]*(count[str(i)]-1)
            if tmp_s_score > tmp_t_score:
                ans_u += count[str(i)]*(count[str(i)]-1)
        else:
            ans += count[str(i)]*count[str(j)]
            if tmp_s_score > tmp_t_score:
                ans_u += count[str(i)]*count[str(j)]

# print(ans_u)
# print(ans)

print(ans_u/ans)
