n = int(input())
dic_a = dict()
dic_b = dict()

for i in range(1, n+1):
    s = str(i)
    if dic_a.get((s[0], s[-1])):
        dic_a[(s[0], s[-1])] += 1
    else:
        dic_a[(s[0], s[-1])] = 1

    if dic_b.get((s[-1], s[0])):
        dic_b[(s[-1], s[0])] += 1
    else:
        dic_b[(s[-1], s[0])] = 1

ans = 0
for key in dic_a.keys():
    if dic_b.get(key):
        inter = dic_b[key] * dic_a[key]
        ans += inter

print(ans)
