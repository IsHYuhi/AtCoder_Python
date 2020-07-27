from collections import Counter
n, m = map(int, input().split())
ka = [list(map(int, input().split())) for _ in range(n)]

foods = [0]*m
for i in ka:
    for j in i[1:]:
        foods[j-1] += 1

foods = Counter(foods)
print(foods[n])
