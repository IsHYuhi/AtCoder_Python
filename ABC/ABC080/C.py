from itertools import combinations
n = int(input())

f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]


li = [i for i in range(10)]
pro_count = -float('inf')

for i in range(1,11):
    iteration = list(combinations(li, i))
    for j in iteration:
        profit = 0
        for l in range(n):
            count = 0
            for k in j:
                if f[l][k]==1:
                    count += 1
            profit += p[l][count]
        pro_count = max(pro_count, profit)

print(pro_count)
