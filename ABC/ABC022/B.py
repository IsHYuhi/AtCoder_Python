from collections import Counter
n = int(input())

A = []
for _ in range(n):
    a = int(input())
    A.append(a)
A = Counter(A)
keys = [v-1 for k, v in A.items() if v >= 2]
print(sum(keys))