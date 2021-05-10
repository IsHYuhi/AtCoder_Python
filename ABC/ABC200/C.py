from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a = [i%200 for i in a]
c = Counter(a)
ans = 0

for k, v in c.items():
    ans += (v*(v-1))//2

print(ans)