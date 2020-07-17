from collections import Counter
n = int(input())
d = Counter([int(input()) for _ in range(n)])
print(len(d))
