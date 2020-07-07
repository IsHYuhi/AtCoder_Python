from collections import Counter
count = list(map(int, input().split()))
count = Counter(count)
print(len(count))