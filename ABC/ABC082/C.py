from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))

a = [i for i in a.items() if i[0]!=i[1]]
ans = 0

for i, j in a:
    if i>j:
        ans += j
    else:
        ans += j-i

print(ans)